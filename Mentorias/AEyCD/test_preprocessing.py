"""Comprobaciones del aislamiento del target y del contrato fit/transform."""

import unittest

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline

from preprocessing import FEATURE_COLUMNS, TARGET, make_preprocessor


class PreprocessingTests(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'PERIOD': np.arange(40) + 90.0,
            'INCLINATION': np.arange(40) + 20.0,
            'APOGEE': np.arange(40) + 600.0,
            'PERIGEE': np.arange(40) + 500.0,
            'LAUNCH_YEAR': np.arange(40) % 10 + 2010,
            'LAUNCH_MASS_KG': np.arange(40) * 5.0 + 100,
            'RCS_SIZE': ['SMALL', 'LARGE'] * 20,
            'COUNTRY': ['A', 'B', 'C', 'D', 'E'] * 8,
            'PURPOSE': ['COMMUNICATIONS', 'EARTH OBSERVATION'] * 20,
            'CLASS_OF_ORBIT': ['LEO', 'GEO'] * 20,
            TARGET: np.arange(40) + 1,
            'INFO_NORAD_NUMBER': np.arange(40) + 1000,
        })
        self.data.loc[[2, 8], 'LAUNCH_MASS_KG'] = np.nan
        self.data.loc[4, 'PERIOD'] = np.nan

    def test_target_and_metadata_cannot_change_predictors(self):
        altered = self.data.copy()
        altered[TARGET] = altered[TARGET] * -1000
        altered['INFO_NORAD_NUMBER'] = -1
        first = make_preprocessor().fit_transform(self.data)
        second = make_preprocessor().fit_transform(altered)
        np.testing.assert_allclose(first, second)

    def test_transform_handles_new_values_without_learning(self):
        preprocessor = make_preprocessor().fit(self.data[FEATURE_COLUMNS])
        reference = preprocessor.transform(self.data[FEATURE_COLUMNS])
        learned_min = preprocessor.named_steps['scale'].data_min_.copy()
        learned_max = preprocessor.named_steps['scale'].data_max_.copy()
        new = self.data[FEATURE_COLUMNS].iloc[:3].copy()
        new['COUNTRY'] = 'NEW_COUNTRY'
        new['PURPOSE'] = 'NEW_PURPOSE'
        new['CLASS_OF_ORBIT'] = 'NEW_ORBIT'
        new['PERIOD'] = [np.nan, 10000.0, 95.0]
        new['LAUNCH_MASS_KG'] = np.nan
        result = preprocessor.transform(new)
        self.assertTrue(np.isfinite(result).all())
        self.assertEqual(result.shape[0], 3)
        np.testing.assert_allclose(reference, preprocessor.transform(self.data[FEATURE_COLUMNS]))
        np.testing.assert_array_equal(learned_min, preprocessor.named_steps['scale'].data_min_)
        np.testing.assert_array_equal(learned_max, preprocessor.named_steps['scale'].data_max_)
        # La mediana procede del entrenamiento; el extremo nuevo no la cambia.
        period_index = list(preprocessor.get_feature_names_out()).index('numeric__PERIOD')
        unscaled = preprocessor.named_steps['scale'].inverse_transform(result)
        self.assertAlmostEqual(unscaled[0, period_index], self.data['PERIOD'].median())

    def test_raw_frames_work_inside_cross_validation(self):
        pipeline = Pipeline([
            ('preprocess', make_preprocessor()), ('model', DummyClassifier()),
        ])
        result = cross_validate(
            clone(pipeline), self.data[FEATURE_COLUMNS], np.arange(40) % 2,
            cv=StratifiedKFold(2, shuffle=True, random_state=42),
            return_estimator=True, error_score='raise',
        )
        self.assertEqual(len(result['estimator']), 2)
        self.assertIsNot(result['estimator'][0]['preprocess'], result['estimator'][1]['preprocess'])


if __name__ == '__main__':
    unittest.main()

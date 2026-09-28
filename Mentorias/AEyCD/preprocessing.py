"""Preprocesamiento de atributos de satélites, ajustable dentro de cada fold.

La variable objetivo y las columnas INFO_* se excluyen explícitamente.
Los CSV de TP2 conservan unidades originales y valores faltantes.
"""

from sklearn.compose import ColumnTransformer
from sklearn.experimental import enable_iterative_imputer  # noqa: F401
from sklearn.impute import IterativeImputer, SimpleImputer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, OrdinalEncoder

TARGET = "EXPECTED_LIFETIME_YRS"
NUMERIC_MEDIAN_FEATURES = ["PERIOD", "INCLINATION", "APOGEE", "PERIGEE", "LAUNCH_YEAR"]
MASS_FEATURE = "LAUNCH_MASS_KG"
FEATURE_COLUMNS = NUMERIC_MEDIAN_FEATURES + [
    MASS_FEATURE, "RCS_SIZE", "COUNTRY", "PURPOSE", "CLASS_OF_ORBIT"
]


def make_preprocessor(random_state: int = 42) -> Pipeline:
    """Devuelve un preprocesador nuevo, sin ajustar.

    Medianas y categorías se aprenden sólo en ``fit``. La masa se imputa
    mediante IterativeImputer con KNeighborsRegressor tras escalar los
    atributos. EXPECTED_LIFETIME_YRS nunca participa de esa imputación.

    Para evaluar un modelo, incluir este objeto y el estimador en un mismo
    Pipeline y pasar los datos sin transformar a cross_validate/BayesSearchCV.
    No reutilizar las matrices de demostración de TP2 en validación cruzada.
    """
    nominal = Pipeline([
        ("missing", SimpleImputer(strategy="constant", fill_value="UNKNOWN")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])
    country = Pipeline([
        ("missing", SimpleImputer(strategy="constant", fill_value="UNKNOWN")),
        ("onehot", OneHotEncoder(
            max_categories=5, handle_unknown="infrequent_if_exist", sparse_output=False
        )),
    ])
    radar = Pipeline([
        ("missing", SimpleImputer(strategy="most_frequent")),
        ("ordinal", OrdinalEncoder(
            categories=[["SMALL", "MEDIUM", "LARGE"]],
            handle_unknown="use_encoded_value", unknown_value=-1,
        )),
    ])
    columns = ColumnTransformer([
        ("numeric", SimpleImputer(strategy="median", keep_empty_features=True),
         NUMERIC_MEDIAN_FEATURES),
        ("mass", "passthrough", [MASS_FEATURE]),
        ("radar", radar, ["RCS_SIZE"]),
        ("country", country, ["COUNTRY"]),
        ("nominal", nominal, ["PURPOSE", "CLASS_OF_ORBIT"]),
    ], remainder="drop", verbose_feature_names_out=True)
    return Pipeline([
        ("columns", columns),
        ("scale", MinMaxScaler()),
        ("impute_mass", IterativeImputer(
            estimator=KNeighborsRegressor(n_neighbors=5),
            initial_strategy="median", max_iter=20, skip_complete=True,
            random_state=random_state, keep_empty_features=True,
        )),
    ])

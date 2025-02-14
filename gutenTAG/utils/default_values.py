from typing import Any, Dict

from .global_variables import BASE_OSCILLATIONS, ANOMALIES, PARAMETERS


default_values: Dict[str, Dict[str, Any]] = {
    BASE_OSCILLATIONS: {
        PARAMETERS.LENGTH: 10000,
        PARAMETERS.KIND: "sine",
        PARAMETERS.FREQUENCY: 10.0,
        PARAMETERS.AMPLITUDE: 1.0,
        PARAMETERS.VARIANCE: 0.0,
        PARAMETERS.AVG_PATTERN_LENGTH: 10,
        PARAMETERS.VARIANCE_PATTERN_LENGTH: 0.0,
        PARAMETERS.VARIANCE_AMPLITUDE: 2.0,
        PARAMETERS.FREQ_MOD: 0.0,
        PARAMETERS.POLYNOMIAL: [1, 1],
        PARAMETERS.TREND: None,
        PARAMETERS.OFFSET: 0.0,
        PARAMETERS.SMOOTHING: 0.01,
        PARAMETERS.CHANNEL_DIFF: 0.0,
        PARAMETERS.CHANNEL_OFFSET: 1.0,
        PARAMETERS.RANDOM_SEED: None,
        PARAMETERS.FORMULA: None,
        PARAMETERS.ECG_SIM_METHOD: "simple",
        PARAMETERS.WIDTH: 1.0,
        PARAMETERS.DUTY: 0.5,
        PARAMETERS.PERIODICITY: 6,
        PARAMETERS.COMPLEXITY: 7,
        PARAMETERS.INPUT_TIMESERIES_PATH_TRAIN: None,
        PARAMETERS.INPUT_TIMESERIES_PATH_TEST: None,
        PARAMETERS.USE_COLUMN_TRAIN: None,
        PARAMETERS.USE_COLUMN_TEST: None
    },
    ANOMALIES: {
        PARAMETERS.LENGTH: 200,
        PARAMETERS.POSITION: "middle",
        PARAMETERS.CHANNEL: 0,
        PARAMETERS.CREEPING_LENGTH: 0
    }
}

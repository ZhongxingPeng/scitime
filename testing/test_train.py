import unittest
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from scikest.train import Trainer


class TestTrain(unittest.TestCase):
    inputs, outputs = None, None

    def setUp(self):
        self.rf_trainer = Trainer(drop_rate=0.99999, verbose=0, algo='RandomForestRegressor')
        self.svc_trainer = Trainer(drop_rate=0.999999, verbose=0, algo='SVC')
        self.km_trainer = Trainer(drop_rate=0.99, verbose=0, algo='KMeans')

    def test_generate_data_supervised(self):
        rf_inputs, rf_outputs = self.rf_trainer._generate_data()

        TestTrain.rf_inputs = rf_inputs
        TestTrain.rf_outputs = rf_outputs

        assert rf_inputs.shape[0] > 0
        assert rf_outputs.shape[0] > 0

    def test_generate_data_classification(self):
        svc_inputs, svc_outputs = self.svc_trainer._generate_data()

        TestTrain.svc_inputs = svc_inputs
        TestTrain.svc_outputs = svc_outputs

        assert svc_inputs.shape[0] > 0
        assert svc_outputs.shape[0] > 0

    def test_generate_data_unsupervised(self):
        km_inputs, km_outputs = self.km_trainer._generate_data()

        TestTrain.km_inputs = km_inputs
        TestTrain.km_outputs = km_outputs

        assert km_inputs.shape[0] > 0
        assert km_outputs.shape[0] > 0

    def test_model_fit_supervised(self):
        rf_meta_algo = self.rf_trainer.model_fit(generate_data=False, df=TestTrain.rf_inputs,
                                                 outputs=TestTrain.rf_outputs)
        assert type(rf_meta_algo).__name__ == 'RandomForestRegressor'

    def test_model_fit_classification(self):
        svc_meta_algo = self.svc_trainer.model_fit(generate_data=False, df=TestTrain.svc_inputs,
                                                   outputs=TestTrain.svc_outputs)
        assert type(svc_meta_algo).__name__ == 'RandomForestRegressor'

    def test_model_fit_unsupervised(self):
        km_meta_algo = self.km_trainer.model_fit(generate_data=False, df=TestTrain.km_inputs,
                                                 outputs=TestTrain.km_outputs)

        assert type(km_meta_algo).__name__ == 'RandomForestRegressor'


if __name__ == '__main__':
    unittest.main()

import tensorflow as tf

from graphs.basics.AE_graph import create_graph, encode_fn
from training.autoencoding_basic.autoencoders.autoencoder import autoencoder as basicAE


class autoencoder(basicAE):
    def __init__(
            self,
            name,
            inputs_shape,
            outputs_shape,
            latents_dim,
            variables_params,
            filepath=None
    ):

        basicAE.__init__(self,
                         name=name,
                         inputs_shape=inputs_shape,
                         outputs_shape=outputs_shape,
                         latents_dim=latents_dim,
                         variables_params=variables_params,
                         filepath=filepath,
                         model_fn=create_graph
                         )

        self.encode_graph = encode_fn

    @tf.function
    def feedforwad(self, inputs):
        X = inputs[0]
        y = inputs[1]
        z = self.__encode__(X)
        x_logit = self.decode(tf.concat[z, y])
        return {'x_logit': x_logit, 'z_latents': z}


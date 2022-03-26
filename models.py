from astropy.modeling.models import Sersic2D
from astropy.modeling.parameters import Parameter
import numpy as np


class Sersic2DAsym(Sersic2D):
    """
    Two dimensional Sersic profile with asymmetry.

    Parameters are same as Sersic2D, plus:
    ----------
    asym_strength : float, optional
        Strength of asymmetry.
    asym_angle : float, optional
        Position angle of maximum asymmetry.


    Notes
    -----
    Asymmetry introduced by multiplying Sersic2D profile by
    (1 - asym_strength * cosine(theta - asym_angle)
    where theta is the position angle of the profile.
    """

    asym_strength = Parameter(default=0)
    asym_angle = Parameter(default=0)

    @classmethod
    def evaluate(cls, x, y, amplitude, r_eff, n, x_0, y_0, ellip, theta,
                 asym_strength, asym_angle):
        """Two dimensional Sersic profile function with asymmetry."""

        if cls._gammaincinv is None:
            try:
                from scipy.special import gammaincinv
                cls._gammaincinv = gammaincinv
            except ValueError:
                raise ImportError('Sersic2DAsym model requires scipy > 0.11.')

        bn = cls._gammaincinv(2. * n, 0.5)
        a, b = r_eff, (1 - ellip) * r_eff
        cos_theta, sin_theta = np.cos(theta), np.sin(theta)
        x_maj = (x - x_0) * cos_theta + (y - y_0) * sin_theta
        x_min = -(x - x_0) * sin_theta + (y - y_0) * cos_theta
        z = np.sqrt((x_maj / a) ** 2 + (x_min / b) ** 2)
        eps = 1e-32
        angle = np.arctan(x_maj/(x_min + eps))
        angle += np.pi * (x_min < 0) - np.pi/2
        angle[np.isnan(angle)] = 0
        asym = (1 - asym_strength * np.cos(asym_angle - angle))
        return amplitude * asym * np.exp(-bn * (z ** (1 / n) - 1))


    def _parameter_units_for_data_units(self, inputs_unit, outputs_unit):
        par_unit = super()._parameter_units_for_data_units(inputs_unit, outputs_unit)
        return par_unit + {'asym_angle': u.rad}

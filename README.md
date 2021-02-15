# extra-astropy-models

Some additional models based on [`astropy.modeling`](astropy.modeling).

These are for my own use, but made available in case they are useful
for others. Ultimately, I hope to contribute these for inclusion in [`astropy.modeling`][astropy.modeling].

Currently the only model implemented is a simple asymmetric version of the
2D Sérsic profile.

It may be better for this to be implemented as a wrapper that adds
asymmetry to any 2D profile.

I also plan to add a 2D "higher-order Sérsic" profile suggested by
[René Andrae, Peter Melchior and Knud Jahnke (2011)](AMJ11) (see
appendix A2). The regular Sérsic profile is characterised by a single
'index' (n), which determines the profile shape at both large and
small radii. The higher-order version extends the regular Sérsic
profile, using Taylor expansion arguments, such that the behaviours at
small and large radii are decoupled.

[astropy.modeling]: https://github.com/astropy/astropy/tree/master/astropy/modeling
[AMJ11]: https://ui.adsabs.harvard.edu/abs/2011MNRAS.417.2465A/abstract

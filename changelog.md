# Versioning

The versioning scheme using in this project is based on Semantic Versioning, but adopts a different approach to handling pre-releases and build metadata.

The essence of semantic versioning is a 3-part MAJOR.MINOR.MAINTENANCE numbering scheme, where the project author increments:

* MAJOR version when they make incompatible API changes,

* MINOR version when they add functionality in a backwards-compatible manner, and

* MAINTENANCE version when they make backwards-compatible bug fixes.


# History

## Version 0.1.2

**New Features**

**Bugfixes**
* Multiple calls to .rotate(angle) do not rotate the ports anymore while keeping the unit itself at the same angle.



## Version 0.1.1 (27-12-2020)
* Alpha version
* Basic drawing functions implemented
* [svgwrite](https://github.com/mozman/svgwrite) backend for vector output
* Limited library of unit operations
  * Mixer / Splitter
  * Heat Exchanger
  * Vessel (vertical/horizontal)
  * Distillation Column (optional reboiler and condenser, some internals)
  * Pump
  * Stream flag / Feed / Product
  * Valve
  * BlackBox Unit Operation (catch all for non-implemented icons)
* Arbitary Rotation
* Horizontal Flipping
* Stream routing via Dykstra algorithm (using the  [python-pathfinding package](https://github.com/brean/python-pathfinding) )


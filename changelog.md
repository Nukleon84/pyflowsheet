# Versioning

The versioning scheme using in this project is based on Semantic Versioning, but adopts a different approach to handling pre-releases and build metadata.

The essence of semantic versioning is a 3-part MAJOR.MINOR.MAINTENANCE numbering scheme, where the project author increments:

* MAJOR version when they make incompatible API changes,

* MINOR version when they add functionality in a backwards-compatible manner, and

* MAINTENANCE version when they make backwards-compatible bug fixes.


# History

## Version 0.2.0 (03-01-2021)

**New Features**
* Added an "Internals" System. You can now add any instance derived from BaseInternal to the internals list of a unit operation. These internals can represent tubes in a heat exchanger, trays or packing in a column, or special realisations of pumps and compressors. 

  **Breaking Change**: It is not possible to define internals by a string anymore.
```python 
U3=pfd.unit(Vessel("Fermenter","Fermenter", position=(200,190), capLength=20, showCapLines=False, size=(80,140),internals=[Stirrer(type=StirrerType.Anchor), Jacket()] ))
```
* Changed how vertical/horizontal vessels work: Now every vessel is vertical by default, but can be rotated either with the rotate(angle) method or by passing the angle as parameter into the constructor.
```python
BA11=Vessel("DS10-BA11","Horizontal Vessel", angle=90, position=(560,400), size=(40,100), capLength=20,internals=[CatalystBed()] )
```
* Compressor unit operation

**Bugfixes**
* Multiple calls to .rotate(angle) do not rotate the ports anymore while keeping the unit itself at the same angle.
* Rotating a unit now influences the area that is blocked for pathfinding.



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


<!--
===============================================
vidgear library source-code is deployed under the Apache 2.0 License:

Copyright (c) 2019 Abhishek Thakur(@abhiTronix) <abhi.una12@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
===============================================
-->

# ScreenGear API Parameters 

&thinsp;

## **`monitor`**

This parameter enables [`mss`](https://github.com/BoboTiG/python-mss) usage and is most suitable for selecting index of a specific screen _(from where you want retrieve frames)_ in multi-monitor setup. For example, its value can be assign to `2`, to fetch frames from a secondary monitor screen. More information can be found [here ➶](https://python-mss.readthedocs.io/api.html#mss.tools.mss.base.MSSBase.monitors)

!!! tip "You can assign `monitor` value to `-1` to fetch frames from all connected multiple monitor screens."

!!! warning "Implication of using `monitor` parameter"
    Any value on `monitor` parameter other than `None` in ScreenGear API: 
    
    * Will force `mss` library backend.
    * Will output [`BGRA`](https://en.wikipedia.org/wiki/RGBA_color_model) colorspace frames instead of default `BGR`. 
    * Will disable the [`backend`](../params/#backend) parameter.


**Data-Type:** Integer

**Default Value:** Its default value is `None` _(i.e. disabled by default)_.

**Usage:**

```python
ScreenGear(monitor=-1) # to fetch frames from all connected multiple screens
```

&nbsp;

## **`backend`**

This parameter enables [`pyscreenshot`](https://github.com/BoboTiG/python-mss) usage and select suitable backend for extracting frames in ScreenGear. The user have the authority of selecting suitable backend which generates best performance as well as the most compatible with their machines. The possible values are: `pil`, `mss`, `scrot`, `maim`, `imagemagick`, `pyqt5`, `pyqt`, `pyside2`, `pyside`, `wx`, `pygdk3`, `mac_screencapture`, `mac_quartz`, `gnome_dbus`, `gnome-screenshot`, `kwin_dbus`. *More information on these backends can be found [here ➶](https://github.com/ponty/pyscreenshot)*

!!! note "Performance Benchmarking of each backend can be found [here ➶](https://github.com/ponty/pyscreenshot#performance)"

!!! warning "Remember to install backend library and all of its dependencies you're planning to use with ScreenGear API."

!!! error "Any value on [`monitor`](#monitor) parameter will disable the `backend` parameter. You cannot use both parameters at same time."

**Data-Type:** String

**Default Value:** Its default value is `""` _(i.e. default backend)_.

**Usage:**

```python
ScreenGear(backend="mss") # to enforce `mss` as backend for extracting frames.
```

&nbsp;

## **`colorspace`**

This parameter selects the colorspace of the source stream. 

**Data-Type:** String

**Default Value:** Its default value is `None`. 

**Usage:**

!!! tip "All supported `colorspace` values are given [here ➶](../../../bonus/colorspace_manipulation/)."

```python
ScreenGear(colorspace="COLOR_BGR2HSV")
```

!!! example "Its complete usage example is given [here ➶](../usage/#using-screengear-with-direct-colorspace-manipulation)"

&nbsp;


## **`options`** 

This parameter provides the flexibility to manually set the dimensions of capture screen area. 

!!! info "Supported Dimensional Parameters"

	Supported Dimensional Parameters are as follows: 

	* **`left`:** the x-coordinate of the upper-left corner of the region
	* **`top`:** the y-coordinate of the upper-left corner of the region
	* **`width`:** the width of the region
	* **`height`:** the height of the region

!!! note "Additional Exclusive Attribute such as [`THREAD_TIMEOUT`](../../camgear/advanced/source_params/#exclusive-camgear-parameters) is also supported for this parameter."


**Data-Type:** Dictionary

**Default Value:** Its default value is `{}` 

**Usage:**

The desired dimensional parameters can be passed to ScreenGear API by formatting them as attributes, as follows:

!!! tip "More information about screen dimensioning can be found [here ➶](https://python-mss.readthedocs.io/api.html#mss.tools.mss.base.MSSMixin.monitors)"

```python
# formatting dimensional parameters as dictionary attributes
options = {'top': 40, 'left': 0, 'width': 100, 'height': 100}
# assigning it w.r.t monitor=1
ScreenGear(monitor=1, **options)
```

&nbsp;

## **`logging`**

This parameter enables logging _(if `True`)_, essential for debugging. 

**Data-Type:** Boolean

**Default Value:** Its default value is `False`.

**Usage:**

```python
ScreenGear(logging=True)
```

&nbsp;
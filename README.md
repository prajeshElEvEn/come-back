# Go and Come Back

`Go and Come Back` is a program written in `python` that makes a drone fly and come back to its initial position.

## Resources

- [MAVProxy](https://ardupilot.org/mavproxy/)
- [DroneKit](https://dronekit.io/)
- [DroneKit-SITL](https://dronekit-python.readthedocs.io/en/latest/develop/sitl_setup.html)

<!-- ## Installation -->

## Usage

- Install neccesary dependencies:

```bash
pip install MAVProxy dronekit dronekit-sitl wxPython wheel
```

- Setting up `home` position of `SITL`:

```bash
dronekit-sitl copter --home=LATITUDE,LONGITUDE,0,180
```

- Running `MAVProxy` to connect `SITL` to `Mission Planner`:

```bash
mavproxy --master tcp:127.0.0.1:5760 --out udp:127.0.0.1:14551 --out udp:10.20.1.85:14550
```

- Running `Go and Come Back` script:

```bash
python main.py --connect udp:127.0.0.1:14550
```

## Reference

[Tiziano Fiorenzani](https://youtu.be/TFDWs_DG2QY)

## Author

[@prajeshElEvEn](https://github.com/prajeshElEvEn)

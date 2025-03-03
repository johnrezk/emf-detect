# emf-detector

This is a simple Python script which scans for **21e8 Hz**

## Physical Hardware

- Software defined radio capable of reading up to 3000 Mhz
  - In this implementation I am using a `RTL-SDR Blog V4` and `Nooelec Ham It Down 3GHz Downconverter` to achieve proper readings
  - If you use a different SDR setup, you will need to modify the code
- Discone antenna, preferably in the 25-3000Mhz range
  - Out-of-spec antennas may still work, like the [Taurus Desktop 25-2000 Mhz](https://www.amazon.com/dp/B0C9HZ4GZT)
  - We are simply measuring amplitude, so precise readings are not necessary
- Windows 11 Computer

## Software Prerequesites

- `Python 3.10 - 3.12`
- `pdm`

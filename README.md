# Py-Weather-CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.7+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![CI](https://github.com/webkolog/py-weather-app/actions/workflows/python-tests.yml/badge.svg)](https://github.com/webkolog/py-weather-app/actions)

**Version:** 1.0

**Created Date:** 2026-07-21

**Last Updated:** 2026-07-21

**Compatibility:** Python 3.6+

**Created By:** Ali Candan ([@webkolog](https://github.com/webkolog))

**Website:** [http://webkolog.net](http://webkolog.net)

**Copyright:** (c) 2026 Ali Candan

**License:** MIT License ([http://mit-license.org](http://mit-license.org))

**Py-Weather-CLI** is a lightweight, terminal-based weather application that allows you to instantly check the current weather conditions, temperature, and humidity for any city around the globe using the wttr.in JSON API.

## Installation

### 1. Prerequisites
Make sure you have Python 3 installed on your system. You will also need the `requests` library to handle API calls.

### 2. Install Dependencies
Install the required package via pip:
```bash
pip install requests

```

### 3. Download the Script

Save the code as `weather.py` in your project directory.

## Usage

Run the script from your terminal:

```bash
python weather.py

```

### Flow of Operation

* The application will prompt you to enter a city name.
* It sends a structured query to the `wttr.in` backend using the dynamic JSON format.
* It parses the response and prints out clear, scannable terminal outputs.

## Example Usages

### Fetching Weather for a City

When you execute the script, interact with the CLI as shown below:

```text
Enter city name: Istanbul

 City: Istanbul

 Temperature: 26 °C

 Weather: Clear

 Humidity: 54 %

```

## Error Handling & Key Notes

* **Dynamic Inputs:** Ensure you use the correct f-string syntax (`{city}` instead of parenthesized placeholders) in the script URL to let Python properly inject user variables.
* **Network Dependencies:** Since this script fetches live data, an active internet connection is required. If the API is unreachable, the `requests.get()` method will throw a connection error.
* **City Names:** For multi-word cities (e.g., New York), the script handles standard string input smoothly, but encoding space characters or using dashes can help optimize edge-case API results.

## Dependencies

This script relies on the following standard and third-party libraries:

* `requests` (For making HTTP requests to the external API)
* `json` (Built-in, implicitly used by requests to parse JSON format payload data)

## License

This Py-Weather-CLI project is open-source software licensed under the [MIT license](https://mit-license.org/).

```text
MIT License

Copyright (c) 2026 Ali Candan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

## Support

For any questions or support regarding the Py-Weather-CLI script, you can refer to the project's GitHub repository or contact the author.


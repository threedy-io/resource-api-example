## Description:

This script shows how to transcode a 3D asset using the Resource API.

---

## Table of content:

---

- [Description:](#description)
- [Table of content:](#table-of-content)
- [How to use the example](#how-to-use-the-example)
- [Technical details](#technical-details)
- [License](#license)
- [How to report an issue](#how-to-report-an-issue)

---

## How to use the example

- Replace `data_urls` in the script with the file URLs you want to transcode
- Replace `api_base_url` with your URL
- Run `python ResourceAPI.py` to transcode the file and check its progress

## Technical details

- The Resource API consists of 2 endpoints
  - The first POST request triggers the transcoding process
  - The second POST request is used to check the transcoding status.
- More details can be found [here](https://docs.threedy.io/3.6.2/doc/microservices/resource/api.html).

## License

This sample is licensed under the terms of the MIT License. Please see the [LICENSE](./LICENSE) file for full details.

## How to report an issue

If you encounter any issues, please [contact us](mailto:github-threedy@threedy.io).

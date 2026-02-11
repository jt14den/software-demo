# Biodiversity Analysis Toolkit

[![DOI](https://sandbox.zenodo.org/badge/DOI/10.5072/zenodo.439801.svg)](https://handle.test.datacite.org/10.5072/zenodo.439801)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Analysis tools for biodiversity research data. This project demonstrates reproducible research software workflows.

> **Note:** This is a teaching/demo repository. The DOI above points to Zenodo Sandbox for demonstration purposes.

## 📚 Workshop Participants

**New here?** See [FOLLOW_ALONG.md](FOLLOW_ALONG.md) for a step-by-step guide to exploring this repository's six states (01-start → 06-metadata) and understanding how research software becomes FAIR (Findable, Accessible, Interoperable, Reusable).

## Features

- **Reproducible Environment**: Uses [pixi](https://pixi.sh) for cross-platform dependency management
- **Citable**: Includes CITATION.cff and DOI via Zenodo
- **Open Source**: Licensed under BSD 3-Clause

## Getting Started

### Prerequisites

- [pixi](https://pixi.sh) (includes Python and all dependencies)

### Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/jt14den/software-demo.git
   cd software-demo
   ```

2. Install dependencies and run the analysis:
   ```bash
   pixi install
   pixi run python src/analysis.py
   ```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Code of Conduct

Please read and abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Citation

If you use this software, please cite it using the metadata in [CITATION.cff](CITATION.cff) or via the DOI badge above.

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.

## Authors

- Tim Dennis (UCLA)
- Leigh Phan (UCLA)
- Reid Otsuji (UCSD)
- Karla Padilla (UCSD)

## Contact

For questions or feedback, please open an issue in this repository.

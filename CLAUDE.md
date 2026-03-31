# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django project designed to load scientific data from CDF (Common Data Format) files into a PostgreSQL database and visualize the data using Plotly. The project handles spacecraft mission data, particularly focusing on solar physics datasets.

## Core Architecture

The project consists of two main Django apps:

1. **load_cdf** - Handles uploading CDF datasets into the database through a multi-step process
2. **pages** - Handles data visualization and plotting using Plotly
3. **data_cdf** - Dynamically generated models for specific datasets (programmatically accessed only)

### Key Components

- **Dataset Management**: Each dataset is identified by a tag (e.g., INTERBALL_IT_K0_ELE_v01) and consists of CDF files with associated metadata
- **Evaluation Process**: Multi-step process that analyzes dataset structure and creates database schema
- **Data Loading**: Bulk insertion of CDF file data into dynamically generated database tables
- **Visualization**: Interactive plotting of time series and spectrogram data using Plotly

## Common Development Commands

### Setup and Installation
```bash
# Create virtual environment and install dependencies
python -m venv solar_venv
source solar_venv/bin/activate  # On Windows: solar_venv\Scripts\activate
pip install -r venv_requirements

# Configure settings in configs/settings.json with database credentials and paths
# Run initial migrations
python manage.py makemigrations load_cdf --skip-checks
python manage.py migrate load_cdf --skip-checks

# Create available DataType instances (one-time setup)
python manage.py create_datatype
```

### Running the Application
```bash
# Start the development server
python manage.py runserver <ip-address:port>
```

### Data Processing Workflow

1. **Evaluate a dataset** (analyze structure and prepare for loading):
```bash
python manage.py evaluate <zip_filename> <match_file_name>
```

2. **Load data** (after evaluation and migrations):
```bash
python manage.py save_data <upload.u_tag> <dataset.tag>
```

3. **Undo evaluation** (if needed):
```bash
python manage.py undo <upload.u_tag> <dataset.tag>
```

### Testing and Debugging
```bash
# View logs
python manage.py runserver  # Check console output
# Or check the log file specified in settings.json under LOG_FILE
```

## Code Structure Overview

### Main Directories
- `solarterra/` - Main Django project directory
- `solarterra/load_cdf/` - Core data loading functionality
- `solarterra/pages/` - Web interface and plotting
- `solarterra_submodules/data_cdf/` - Dynamically generated dataset models
- `configs/` - Configuration files
- `examples/` - Sample CDF files and documentation

### Key Models (in load_cdf/models.py)
- **Upload** - Tracks each data upload attempt
- **Dataset** - Represents a collection of related CDF files
- **Variable** - Individual data variables within datasets
- **DynamicModel/DynamicField** - Maps CDF variables to database fields
- **DataType** - CDF data type definitions and conversions

### Management Commands (in solarterra/load_cdf/management/commands/)
- `evaluate.py` - Main entry point for dataset evaluation (calls sub-commands 010-018)
- `save_data.py` - Loads CDF file data into database
- `undo.py` - Reverses evaluation steps
- `create_datatype.py` - Initializes data type mappings

### Data Flow
1. CDF files + match files → Evaluation process → Database schema creation
2. Schema migration → Data loading → PostgreSQL storage
3. Database queries → Plotly visualization → Web interface

## Development Notes

- PostgreSQL is required (not compatible with SQLite)
- The system generates dynamic Django models for each dataset type
- Large datasets are processed with bulk insert operations for performance
- Time-series and spectrogram data visualization supported
- Extensive logging to both file and database for troubleshooting
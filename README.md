# onshnap

`onshnap` exports Onshape assemblies as static URDF or MJCF files with STL meshes. Takes a frozen snapshot of the assembly and exports it as a fixed robot description file.

## Features

- **Frozen Snapshot Export**: Exports assemblies as static robot descriptions (no kinematic chains)
- **Star Topology**: All parts connected to a single base_link via fixed joints
- **Multiple Formats**: Supports URDF and MJCF output formats
- **Color Support**: Extracts and preserves part colors from Onshape
- **Mass Properties**: Extracts mass and inertia information when available

### Usage
```bash
export ONSHAPE_ACCESS_KEY="your-access-key"
export ONSHAPE_SECRET_KEY="your-secret-key"
onshnap /path/to/directory/with/config
```

### Configuration
The config.json should contain:
```json
{
    "url": "https://cad.onshape.com/documents/...",
    "filetype": "urdf", // optional, defaults to "urdf"
    "output_name": "onshnap", // optional, defaults to "onshnap"
    "mesh_dir": "meshes", // optional, defaults to "meshes"
    "units": "meter" // optional, defaults to "meter"
}
```

**Configuration Options:**
- `url` (required): Onshape document URL
- `filetype` (optional): Output format - `"urdf"` (default) or `"mjcf"`
- `output_name` (optional): Base name for output files (default: `"onshnap"`)
- `mesh_dir` (optional): Subdirectory name for mesh files (default: `"meshes"`)
- `units` (optional): Units for mesh export - `"meter"` (default) or `"inch"`

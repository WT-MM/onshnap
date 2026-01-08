# onshnap

`onshnap` exports Onshape assemblies as static URDF files with STL meshes. Takes a frozen snapshot of the assembly and exports it as a fixed URDF file.


### Usage
```bash
export ONSHAPE_ACCESS_KEY="your-access-key"
export ONSHAPE_SECRET_KEY="your-secret-key"
onshnap /path/to/directory/with/config.json
```

### Configuration
The config.json should contain:
```json
{
    "url": "https://cad.onshape.com/documents/..."
}
```

# Changelog

## [1.1.0] ->  [2.0.0] - 2025-10-06

### ✨ Added
- **Abstract Base Class Architecture**
  - `Systorage` is now an abstract base class with abstract methods
  - Enforced implementation of `create()`, `delete()`, and `get_size()` methods
  - Abstract method `_update_metadata()` for metadata management

- **Advanced File and Directory Operations**
  - `rename(new_name: str)` method for renaming files and directories
  - `move(new_path: str)` method for moving files and directories
  - Automatic parent-child relationship binding with `__bind_as_parent()`
  - `get_parent()` method to access parent directory objects

- **Unified Search API with SearchOptions**
  - `SearchOptions` class for consistent search parameter handling
  - Support for recursion, segmentation, and extension filtering
  - Automatic extension parsing from enum values and strings
  - Property-based access to search parameters

- **Segmented Search Results**
  - `SegmentedSearchResult` class for organized search results
  - Parent-child relationship representation in search results
  - `to_paths()` method for converting results to path dictionaries
  - Enhanced segmentation with proper parent grouping

- **Enhanced Path Management**
  - Improved `Path` class with `get_complex()` method for pathlib.Path access
  - Better path formatting with `format_path()` method
  - Absolute path resolution with `os.path.realpath()`
  - Cross-platform path normalization

### 🔧 Changed
- **Breaking API Changes**
  - All search methods now use `SearchOptions` instead of individual parameters
  - `Directory` constructor parameters changed: `auto_load` and `recursive_load` are now separate
  - Method signatures updated to use the new options system
  - Return types changed to use `SegmentedSearchResult` for segmented operations

- **Improved Directory Loading**
  - Enhanced `load()` method with separate `auto_load` and `recursive_load` parameters
  - Better file and directory loading with `__load_files()` and `__load_directories()`
  - Automatic parent binding for all loaded elements
  - More efficient recursive loading implementation

- **File Operations Enhancement**
  - `delete()` method now supports `delete_content` parameter with validation
  - Improved error handling for content deletion operations
  - Better file size calculation with `get_size()` method
  - Enhanced content management with `delete_content()` method

### 🗑️ Removed
- **Legacy API Methods**
  - Old parameter-based search methods replaced with `SearchOptions`
  - Direct extension filtering parameters removed in favor of unified options
  - Simplified method signatures with fewer individual parameters

### 🛠️ Technical
- **Code Organization**
  - Modular utility classes in `pyfile/utils/` package
  - Separate files for `SearchOptions` and `SegmentedSearchResult`
  - Cleaner import structure with explicit utility imports
  - Better separation of concerns between classes

- **Type Safety Improvements**
  - Enhanced type hints with proper generic types
  - Better type annotations for method parameters and return values
  - Support for union types in search result handling
  - Improved type safety for extension filtering

- **Performance Optimizations**
  - More efficient recursive operations with dedicated methods
  - Better memory management for large directory structures
  - Optimized parent-child relationship handling
  - Improved path resolution performance

### 🔄 Compatibility
- **Breaking Changes**
  - This version introduces breaking changes to the API
  - Existing code using the old parameter-based methods will need updates
  - Migration guide recommended for users upgrading from 1.x
  - New abstract methods require implementation in custom classes

## [2.0.0] -> [2.1.0]

### ✨ Added

- **Implementations**
  - `Directory` class has now behavior for `delete` method
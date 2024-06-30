RPM Package for the Intel GNA library 
=====================================

This is (the code for an RPM package of) the user space component of the Intel GNA driver for Linux. A [kernel module](https://github.com/xanderlent/intel-gna-kmod) is also required to use the Intel GNA hardware.

See the [upstream intel/gna repository](https://github.com/intel/gna) for more information about the hardware and software.

All patches to the sources are generated from [the fix-fedora-build branch of my downstream fork xanderlent/gna](https://github.com/xanderlent/gna/tree/fix-fedora-build).

### Kernel Header Versioning

Note that the Intel GNA library source code includes its own copy of the `gna_drm.h` header provided by the kernel module, and **is not** built against the system version of that header provided by the kernel module. That means the sources will need to be manually patched to keep things in sync if changes are needed.

(As a TODO, a good patch would be to use the header provided by the kernel module instead of the built-in one. That said, the vendoring of the header lets you build the user space library independently of the kernel, useful for an experimental, out-of-tree driver like this one.)

### Package Availability

[![Copr build status](https://copr.fedorainfracloud.org/coprs/xanderlent/intel-gna-driver/package/gna/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xanderlent/intel-gna-driver/package/gna/)

This package is available for use with Fedora Linux and possibly other RPM-based distributions through my Fedora Copr repository, [xanderlent/intel-gna-driver](https://copr.fedorainfracloud.org/coprs/xanderlent/intel-gna-driver). See that page for information on how to install and use this software on Fedora Linux (and possibly other RPM-based distributions).

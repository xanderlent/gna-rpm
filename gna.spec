Name:           gna
Version:        3.0.0
Release:        3%{?dist}
Summary:        Intel Gaussian & Neural Accelerator Library

License:        LGPL-2.1-or-later AND (GPL-2.0-only WITH Linux-syscall-note)
URL:            https://github.com/intel/gna
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Patch0:         0001-HACK-Fix-up-CMake-to-use-correct-directories-on-Fedo.patch
Patch1:         0002-HACK-Disable-debug-symbol-stripping-for-release-buil.patch

# TODO Intel seems to intend for this to be an x86-only library
ExclusiveArch:  i686 x86_64

# Uses cmake to build C & C++, uses DRM headers, links against libpthread
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  glibc-devel
# TODO: Build can also use ninja instead of make...
BuildRequires:  make
# TODO: Do we need libdrm at runtime? Looking at the sources I don't think so...
# TODO: We need libpthread at runtime, so...
Requires:       glibc

%description
The Intel Gaussian & Neural Accelerator is a low-power neural co-processor for
continuous inference at the edge.

When power and performance are critical, the Intel Gaussian & Neural
Accelerator (Intel GNA) provides power-efficient, always-on support. Intel GNA
is designed to deliver AI speech and audio applications such as neural noise
cancellation, while simultaneously freeing up CPU resources for overall system
performance and responsiveness.

GNA library provides an API to run inference on Intel GNA hardware, as well as
in the software execution mode on CPU.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
#Cannot use autosetup, because we need to patch into a subdirectory...
#autosetup was mis-applying the patch to CMakeLists.txt in the main dir
%setup -q
# patch args tell it to ignore the first directory prefix but keep the rest
%patch 0 -p1
%patch 1 -p1


%build
%cmake
%cmake_build


%install
%cmake_install
# TODO: Is this default line necessary
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%{?ldconfig_scriptlets}


%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.*

%files devel
# TODO: Samples and Doxygen for API as devel docs?
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/gna3/gna-config*.cmake

# TODO: Does the check part of the docs apply to us? https://docs.fedoraproject.org/en-US/packaging-guidelines/CMake/

%changelog
* Thu Jun 27 2024 Alexander F. Lent <lx@xanderlent.com> - 3.0.0-3
- Whoops, forgot to include correct changelog in -2
* Thu Jun 27 2024 Alexander F. Lent <lx@xanderlent.com> - 3.0.0-2
- Fix rpmlint issues with package spec file
* Thu Jun 27 2024 Alexander F. Lent <lx@xanderlent.com> - 3.0.0-1
- Initial package for Intel GNA library v3.0.0

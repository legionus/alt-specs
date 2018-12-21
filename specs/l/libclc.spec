Name: libclc
Version: 0.2.0
Release: alt2
Summary: An open source implementation of the OpenCL 1.1 library requirements
License: BSD
Group: System/Libraries
URL: https://libclc.llvm.org

Source: %name-%version.tar

BuildPreReq: /proc
BuildRequires: clang libstdc++-devel llvm-devel lld

%description
libclc is an open source, BSD licensed implementation of the library
requirements of the OpenCL C programming language, as specified by the
OpenCL 1.1 Specification. The following sections of the specification
impose library requirements:

  * 6.1: Supported Data Types
  * 6.2.3: Explicit Conversions
  * 6.2.4.2: Reinterpreting Types Using as_type() and as_typen()
  * 6.9: Preprocessor Directives and Macros
  * 6.11: Built-in Functions
  * 9.3: Double Precision Floating-Point
  * 9.4: 64-bit Atomics
  * 9.5: Writing to 3D image memory objects
  * 9.6: Half Precision Floating-Point

libclc is intended to be used with the Clang compiler's OpenCL frontend.

libclc is designed to be portable and extensible. To this end, it provides
generic implementations of most library requirements, allowing the target
to override the generic implementation at the granularity of individual
functions.

libclc currently only supports the PTX target, but support for more
targets is welcome.


%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

%build
export CFLAGS=" -D__extern_always_inline=inline"
./configure.py \
	--prefix=%_prefix \
	--libexecdir=%_prefix/libexec/clc \
	--pkgconfigdir=%_pkgconfigdir

%ifarch aarch64
sed -i 's|\ -frecord-gcc-switches||' Makefile
%endif
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc LICENSE.TXT README.TXT CREDITS.TXT
%_prefix/libexec/clc

%files devel
%_includedir/clc
%_pkgconfigdir/*.pc

%changelog
* Fri Aug 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt2
- build for aarch64

* Mon Jul 30 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- initial release


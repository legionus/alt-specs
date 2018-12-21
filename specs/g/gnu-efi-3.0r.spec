%define origname gnu-efi
%define flavour 3.0r

Name: %origname-%flavour
Version: %flavour
Release: alt3

Summary: Building EFI applications using the GNU toolchain
# Intel and HP's BSD-like license, except setjmp code coming from GRUB
License: GPL v2+ (setjmp code), BSD-like (all the rest)
Group: Development/Other

Url: http://gnu-efi.sourceforge.net/
Source: http://downloads.sourceforge.net/gnu-efi/%{origname}_%version.orig.tar.gz

BuildRequires: binutils >= 2.17.50.0.14
BuildRequires: gcc >= 4.1.1
Requires: binutils >= 2.17.50.0.14
Requires: gcc >= 4.1.1
ExclusiveArch: %ix86 x86_64 ia64

Summary(pl.UTF-8): Tworzenie aplikacji EFI przy użyciu narzędzi GNU

%set_gcc_version 4.7

%description
GNU-EFI development environment allows to create EFI applications
for IA-64 and x86 platforms using the GNU toolchain.

%description -l pl.UTF-8
Rodowisko programistyczne GNU-EFI umożliwia tworzenie aplikacji EFI
dla platform IA-64 i x86 przy użyciu narzędzi GNU.

%prep
%setup -n %origname-3.0

%build
%ifarch x86_64
CFADD=" -DEFI_FUNCTION_WRAPPER -mno-red-zone"
%else
%ifarch ia64
CFADD=" -mfixed-range=f32-f127"
%else
CFADD=
%endif
%endif
%make -j1 \
	ARCH=$(arch | sed -e 's/i.86/ia32/') \
	CFLAGS="%optflags -fpic -Wall -fshort-wchar -fno-strict-aliasing -fno-merge-constants -fno-stack-protector$CFADD" \
	OBJCOPY=objcopy

%install
%make install INSTALLROOT=%buildroot%prefix

%if "%_lib" != "lib"
mv -f %buildroot%prefix/{lib,%_lib}
%endif

%files
%doc ChangeLog README.* apps
%_libdir/libefi.a
%_libdir/libgnuefi.a
%_libdir/crt0-efi-*.o
%_libdir/elf_*_efi.lds
%_includedir/efi

%changelog
* Wed Mar 01 2017 Michael Shigorin <mike@altlinux.org> 3.0r-alt3
- FTBFS workaround: use gcc4.7

* Mon Nov 25 2013 Michael Shigorin <mike@altlinux.org> 3.0r-alt2
- renamed to gnu-efi-3.0r so that 3.0u could be packaged alongside

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 3.0r-alt1
- 3.0r

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 3.0q-alt1
- built for Sisyphus; these PLD people worked on the spec:
  baggins glen qboosh

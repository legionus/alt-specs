Name: vmfs-tools
Version: 0.2.5
Release: alt1

Summary: Tools to access VMFS filesystems
License: GPLv2+
Group: System/Kernel and hardware

Url: http://glandium.org/projects/vmfs-tools/
Source: %name-%version.tar.gz

# Automatically added by buildreq on Sat Apr 23 2011 (-bi)
BuildRequires: asciidoc docbook-style-xsl libfuse-devel libuuid-devel python-modules-encodings time xsltproc

%description
Tools to access VMFS filesystems.

%package -n libvmfs-devel
Summary: Library to access VMFS filesystems
Group: Development/C

%description -n libvmfs-devel
Static library to access VMFS filesystems.

%prep
%setup

%build
./configure --prefix=/usr
%make_build OPTIMFLAGS="%optflags"

%install
export NO_STRIP=1
%makeinstall

install -d %buildroot%_includedir/vmfs
install -pm0644 libvmfs/*.h %buildroot%_includedir/vmfs/
install -pD -m0644 libvmfs/libvmfs.a %buildroot%_libdir/libvmfs.a

%files
%_sbindir/*
%_man8dir/*

%files -n libvmfs-devel
%_includedir/vmfs
%_libdir/libvmfs.a

%changelog
* Sun Mar 03 2013 Michael Shigorin <mike@altlinux.org> 0.2.5-alt1
- 0.2.5

* Fri Jan 06 2012 Victor Forsiuk <force@altlinux.org> 0.2.1-alt2.snap20111024
- This is (unreleased yet) post-0.2.1 code needed by recent versions of partclone.

* Sat Apr 23 2011 Victor Forsiuk <force@altlinux.org> 0.2.1-alt1
- Initial build.

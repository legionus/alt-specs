Name: ibsim
Summary: InfiniBand fabric simulator for management
Version: 0.7
Release: alt1
License: %gpl2only
Group: Monitoring
Url: http://openfabrics.org

# http://git.openfabrics.org/?p=~halr/ibsim.git;a=summary
Source: %name-%version.tar

Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: libinfiniband-diags-devel

%description
%name provides simulation of infiniband fabric for using with
OFA OpenSM, diagnostic and management tools.

%prep
%setup
%patch1 -p1

%build
%make_build CFLAGS="%optflags %optflags_shared -I. -I../include"

%install
%makeinstall_std \
	prefix=%_prefix libpath=%_libdir binpath=%_bindir

%files
%doc README TODO net-examples scripts
%_libdir/umad2sim
%_bindir/*

%changelog
* Mon May 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7-alt1
- Updated to version 0.7.

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt3
- Rebuilt for debuginfo

* Mon Aug 30 2010 Andriy Stepanov <stanv@altlinux.ru> 0.5-alt2.2
- Rebuild with new libibmad

* Tue Jun 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2.1
- Build for Sisyphus

* Tue Jun 09 2009 Led <led@altlinux.ru> 0.5-alt2
- fixed for build with glibc 2.10

* Tue Apr 14 2009 Led <led@altlinux.ru> 0.5-alt1
- 0.5

* Tue Oct 28 2008 Led <led@altlinux.ru> 0.4-alt1
- initial build

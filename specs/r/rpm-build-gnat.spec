# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
%define oldname fedora-gnat-project-common
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           rpm-build-gnat
Version:        3.12
Release:        alt1_1
Summary:        Files shared by Ada libraries
Summary(sv):    Gemensamma filer för adabibliotek

Group:          System/Libraries
License:        Copyright only
URL:            https://src.fedoraproject.org/cgit/rpms/fedora-gnat-project-common.git
Source1:        directories.gpr.in
Source2:        macros.gnat.in
Source3:        gnat-project.sh
Source4:        gnat-project.csh
Source5:        configure
Source6:        LICENSE
#BuildArch:      noarch

BuildRequires:  sed
Requires:       setup
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=613407:
Requires:       libgnat-devel-static
# macros.gnat requires __global_ldflags:
# An RPM that knows about /usr/lib/rpm/macros.d is required:
# Distribute this package only for architectures where libgnat-static is
# available:
ExclusiveArch:  noarch %{GNAT_arches}
Source44: import.info
Patch33: macros.gnat.in.patch
Provides: fedora-gnat-project-common = %version
Requires: rpm-macros-gnat = %{version}-%{release}
# ("noarch" is included so that the build works.)

%description
The fedora-gnat-project-common package contains files that are used by the GNAT
project files of multiple Ada libraries, and also GNAT-specific RPM macros.

%description -l sv
Paketet fedora-gnat-project-common innehåller filer som används av
GNAT-projektfilerna för flera adabibliotek, samt GNAT-specifika RPM-makron.

%global _GNAT_project_dir /usr/share/gpr
# _GNAT_project_dir is defined here and copied from here to macros.gnat so that
# this package won't build-require itself.



%package -n rpm-macros-gnat
Summary: Set of RPM macros for packaging GNAT applications
Group: Development/Other
BuildArch: noarch

%description -n rpm-macros-gnat
Set of RPM macros for packaging GNAT applications for ALT Linux.
Install this package if you want to create RPM packages that use GNAT.

%prep
%setup -n %{oldname}-%{version} -c -T
cp --preserve=timestamps %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} .
%patch33 -p0


%build
exec_prefix=%{_exec_prefix} bindir=%{_bindir} libexecdir=%{_libexecdir} includedir=%{_includedir} GNAT_project_dir=%{_GNAT_project_dir} ./configure


%install
mkdir --parents %{buildroot}%{_GNAT_project_dir} %{buildroot}%{_sysconfdir}/profile.d %{buildroot}%{_rpmmacrosdir}
cp -p directories.gpr %{buildroot}%{_GNAT_project_dir}/
cp -p gnat-project.sh gnat-project.csh %{buildroot}%{_sysconfdir}/profile.d/
cp -p macros.gnat %{buildroot}%{_rpmmacrosdir}/gnat


%files
%doc --no-dereference LICENSE
%{_GNAT_project_dir}
%config(noreplace) %{_sysconfdir}/profile.d/*

%files -n rpm-macros-gnat
%_rpmmacrosdir/*



%changelog
* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 3.12-alt1_1
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 3.10-alt1_1
- update to new release by fcimport

* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 3.9-alt1_7
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 3.9-alt1_5
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 3.9-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.9-alt1_1
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1_2
- update to new release by fcimport

* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1_1
- update to new release by fcimport

* Tue Nov 19 2013 Igor Vlasenko <viy@altlinux.ru> 3.7-alt1_1
- update to new release by fcimport

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_8
- update to new release by fcimport

* Wed Apr 10 2013 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_7
- update from fc import

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_4
- update to new release by fcimport

* Tue Dec 25 2012 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_3
- initial fc import


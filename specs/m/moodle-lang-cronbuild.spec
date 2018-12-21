# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define moodlebranch %nil

#Name: moodle%moodlebranch-lang-cronbuild
Name: moodle-lang-cronbuild
Version: 0.2.0
Release: %branch_release alt1

Summary: Shell functions for moodle-lang cronbuild scripts
License: %gpl2plus
Group: Development/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: sh-functions
Source1: moodle%moodlebranch.lang.xslt

Requires: %_bindir/moodle-lang-cronbuild-common-sh-functions
Requires: %moodle_lang_cronbuildcommondir
Requires: moodle-lang-cronbuild-common >= 0.1.0
Requires: cronbuild-sh-functions >= 0.1.0
Requires: perl-Gear-Rules >= 0.08-alt4
Requires: xsltproc

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-moodle-lang-cronbuild-common
BuildPreReq: rpm-build-licenses

%description
%summary

%install
install -pD -m644 %SOURCE0 %buildroot%_bindir/%name-sh-functions
install -pD -m644 %SOURCE1 %buildroot%moodle_lang_cronbuildcommondir/moodle%moodlebranch.lang.xslt

find %buildroot%_bindir -type f -print0 \
	| xargs -0 sed -i -r '/^.*%%/{
		s@(^|[^%%])%%moodle_lang_cronbuildcommondir([^a-zA-Z0-9_]|$)@\1%moodle_lang_cronbuildcommondir\2@
		s@(^|[^%%])%%moodlebranch([^a-zA-Z0-9_]|$)@\1%moodlebranch\2@
	}'

%files
%_bindir/*
%moodle_lang_cronbuildcommondir/*

%changelog
* Sun Nov 23 2014 Aleksey Avdeev <solo@altlinux.ru> 0.2.0-alt1
- Fix for the new langpacks site

* Thu Jan 05 2012 Aleksey Avdeev <solo@altlinux.ru> 0.1.2-alt1
- Fix lang branch update

* Tue Dec 20 2011 Aleksey Avdeev <solo@altlinux.ru> 0.1.1-alt1
- Fix lang branch update

* Tue Nov 29 2011 Aleksey Avdeev <solo@altlinux.ru> 0.1.0-alt1
- Pulling maintainer srpms branch

* Mon Nov 14 2011 Aleksey Avdeev <solo@altlinux.ru> 0.0.2-alt1
- Fix update_source()

* Sun Nov 13 2011 Aleksey Avdeev <solo@altlinux.ru> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus

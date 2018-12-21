%define fname uralic

Name: fonts-ttf-%fname
Version: 1.00
Release: alt1.qa1

Summary: TrueType fonts

License: GNU
Group: System/Fonts/True type
Url: http://www.peoples.org.ru/uralic.html

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %url/%name.tar.bz2

Provides: %fname-fonts-ttf
Obsoletes: %fname-fonts-ttf

BuildArch: noarch

BuildRequires: rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

%description
This Package provides a TrueType fonts


%prep
%setup -q -n %name

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc license.txt *.html *.rtf *.pdf

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1.qa1
- NMU: applied repocop patch

* Sun Jun 15 2008 Hihin Ruslan <ruslandh@altlinux.ru> 1.00-alt1
- initial build for ALT Linux Sisyphus

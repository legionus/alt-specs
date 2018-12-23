%define pkgname xml-simple

Name: ruby-%pkgname
Version: 1.1.5
Release: alt1
Summary: A very simple API for XML processing
License: Ruby
Group: Development/Ruby
Url: https://github.com/maik/xml-simple

Source: %pkgname-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
Class XmlSimple offers an easy API to read and write XML. It is
a Ruby translation of Grant McLean's Perl module XML::Simple.
Simply put, it automatically converts XML documents into a Ruby
Hash.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/XmlSimple*

%changelog
* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.12-alt1.2
- Rebuild with new Ruby autorequirements.

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.0.12-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.12-alt1
- [1.0.12]

* Mon Mar 31 2008 Sir Raorn <raorn@altlinux.ru> 1.0.11-alt2
- Rebuilt with rpm-build-ruby

* Mon Jan 07 2008 Sir Raorn <raorn@altlinux.ru> 1.0.11-alt1
- Initial build for ALT Linux


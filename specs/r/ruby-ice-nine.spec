%define  pkgname ice_nine

Name:    ruby-ice-nine
Version: 0.11.2
Release: alt1

Summary: Deep Freeze Ruby Objects
License: MIT
Group:   Development/Ruby
Url:     https://github.com/dkubb/ice_nine

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

%description -l ru_RU.UTF8
Глубокая заморозка объектор Рубина.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%description doc -l ru_RU.UTF8
Файлы сведений для %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Sep 04 2018 Pavel Skrylev <majioa@altlinux.org> 0.11.2-alt1
- Bump to version 0.11.2.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 0.11.1-alt1
- Initial build for Sisyphus

%define  pkgname iostruct

Name:    ruby-%pkgname
Version: 0.0.4
Release: alt1.1

Summary: A Struct that can read/write itself from/to IO-like objects
License: MIT
Group:   Development/Ruby
Url:     http://github.com/zed-0xff/iostruct

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

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
* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.4-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.4-alt1
- Initial build for Sisyphus

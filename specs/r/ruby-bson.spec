%define  pkgname bson-ruby

Name: 	 ruby-bson
Version: 4.3.0
Release: alt1.3

Summary: Ruby Implementation of the BSON Specification (2.0.0+)
License: Apache-2.0
Group:   Development/Ruby
Url:     http://bsonspec.org

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

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
* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.1
- Rebuild with Ruby 2.5.0

* Thu Jan 18 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Tue Sep 19 2017 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- Initial build for Sisyphus

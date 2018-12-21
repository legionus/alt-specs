%define  pkgname fog-google

Name:    ruby-%pkgname
Version: 1.8.1
Release: alt1
Epoch:   1

Summary: Fog for Google Cloud Platform
License: MIT
Group:   Development/Ruby
Url:     https://github.com/fog/fog-google

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
* Tue Nov 13 2018 Pavel Skrylev <majioa@altlinux.org> 1:1.8.1-alt1
- Bump to 1.8.1.

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.0.9-alt1
- Use old version for fog.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- New version.
- Package as gem.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt1
- Initial build for Sisyphus

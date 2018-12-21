%define  pkgname mixlib-config
 
Name: 	 ruby-%pkgname
Version: 2.2.14
Release: alt1
 
Summary: A simple class based Config mechanism, similar to the one found in Chef
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/chef/mixlib-config
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Mixlib::Config provides a class-based configuration object, as used in Chef.

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
* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.14-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.2
- Rebuild for new Ruby autorequirements.

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux

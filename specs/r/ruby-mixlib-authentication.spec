%define  pkgname mixlib-authentication
 
Name: 	 ruby-%pkgname
Version: 2.1.4
Release: alt1
 
Summary: AuthN signing and verification. Appears in both the client and server
License: MIT or Ruby
Group:   Development/Ruby
Url:     https://github.com/chef/mixlib-authentication
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Mixlib::Authentication provides a class-based header signing
authentication object, like the one used in Chef.

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
* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.4-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux

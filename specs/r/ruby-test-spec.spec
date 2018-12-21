# vim: set ft=spec: -*- rpm-spec -*-

%define plugname test-spec

Name: ruby-%plugname
Version: 0.10
Release: alt1.3

Summary: an RSpec-inspired interface on top of Test::Unit
License: Ruby/MIT
Group: Development/Ruby
Url: http://test-spec.rubyforge.org/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
Source: %name-%version.tar

# Automatically added by buildreq on Thu Feb 25 2010 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup ruby-test-unit

%description
test/spec layers an RSpec-inspired interface on top of Test::Unit, so you can
mix TDD and BDD (Behavior-Driven Development).

test/spec is a clean-room implementation that maps most kinds of Test::Unit
assertions to a 'should'-like syntax.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -q
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%check
%ruby_test_unit -Ilib:test test

%files
%doc README ROADMAP TODO
%ruby_sitelibdir/test/*
%_bindir/specrb

%files doc
%ruby_ri_sitedir/Test/Spec
%ruby_ri_sitedir/Test/Unit/UI/SpecDox
%ruby_ri_sitedir/Test/Unit/UI/RDox

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.10-alt1.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.10-alt1.2
- Rebuild with Ruby 2.4.1
- Use stadard macros for tests

* Sat Dec 08 2012 Led <led@altlinux.ru> 0.10-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Feb 24 2010 Timur Batyrshin <erthad@altlinux.org> 0.10-alt1
- Initial build for sisyphus



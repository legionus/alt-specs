%global realname jiffy

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 0.14.8
Release: alt1%ubt
Summary: JSON NIFs for Erlang
Group: Development/Erlang
License: MIT
Url: https://github.com/davisp/jiffy

# https://github.com/davisp/jiffy.git
Source: %name-%version.tar

Patch1: erlang-jiffy-fedora-use-system-double-conversion.patch

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-p1_utils
BuildRequires: gcc-c++
BuildRequires: libdouble-conversion-devel

%description
A JSON parser as a NIF.
This new version is a hand crafted state machine
that does its best to be as quick and efficient as possible
while not placing any constraints on the parsed JSON.

%prep
%setup
%patch1 -p1
rm -rf c_src/double-conversion

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14.8-alt1%ubt
- Initial build for ALT.

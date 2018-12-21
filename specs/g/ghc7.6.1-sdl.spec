%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name SDL
%define f_pkg_name sdl
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.6.4
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/SDL
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Binding to libSDL



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1 ghc7.6.1-doc libSDL-devel

%description
Simple DirectMedia Layer \(libSDL\) is a cross-platform multimedia library
designed to provide low level access to audio, keyboard, mouse, joystick,
3D hardware via OpenGL, and 2D video framebuffer. It is used by MPEG
playback software, emulators, and many popular games, including the award
winning Linux port of \"Civilization: Call To Power.\"

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.6.4-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.6.4-alt1
- Spec created by cabal2rpm 0.20_08

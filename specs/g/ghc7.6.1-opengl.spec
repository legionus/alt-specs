%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name OpenGL
%define f_pkg_name opengl
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.6.0.1
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://www.haskell.org/haskellwiki/Opengl
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A binding for the OpenGL graphics system



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common ghc7.6.1-openglraw libGL-devel libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-gluraw ghc7.6.1-hscolour ghc7.6.1-objectname ghc7.6.1-statevar ghc7.6.1-tensor libGLU-devel

%description
A Haskell binding for the OpenGL graphics system (GL, version 3.2) and its
accompanying utility library (GLU, version 1.3).

OpenGL is the industry's most widely used and supported 2D and 3D graphics
application programming interface (API), incorporating a broad set of
rendering, texture mapping, special effects, and other powerful
visualization functions. For more information about OpenGL and its various
extensions, please see <http://www.opengl.org/> and
<http://www.opengl.org/registry/>.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.6.0.1-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.6.0.1-alt1
- Spec created by cabal2rpm 0.20_08

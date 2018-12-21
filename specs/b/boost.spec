
%define boost_include %_includedir/%name
%define boost_doc %_docdir/%name

%def_with devel
%if_with devel
%def_with jam
%def_with devel_static
%else
%def_without jam
%def_without devel_static
%endif

%def_with strict_deps
%def_with python3

# Add compatibility links for boost-python-devel and boost-python3-devel
# TODO: consider removing them later
%def_with python_compat_symlinks

# mpi
%ifarch e2k
%def_without mpi
%else
%def_with mpi
%endif

# long_double
%ifarch %arm
%def_without long_double
%else
%def_with long_double
%endif

# context
%ifarch e2k
%def_without context
%else
%def_with context
%endif

%if_with mpi
%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%endif

%define ver_maj 1
%define ver_min 67
%define ver_rel 0

%define namesuff %{ver_maj}_%{ver_min}_%ver_rel

%define _unpackaged_files_terminate_build 1

Name: boost
Epoch: 1
Version: %ver_maj.%ver_min.%ver_rel
Release: alt5

Summary: Boost libraries
License: Boost Software License
Group: Development/C++
Url: http://www.boost.org

Source: boost-%version.tar
Patch4: boost-1.57.0-alt-explicit-st.patch
Patch5: boost-1.57.0-alt-bjam-locate-target.patch
Patch15: boost-1.36.0-alt-test-include-fix.patch
Patch23: boost-1.45.0-alt-mpi-mt-only.patch
Patch28: boost-1.50.0-fedora-polygon-fix-gcc47.patch
Patch29: boost-1.53.0-alt-qt4-moc-fix.patch
Patch30: boost-1.63.0-alt-python-paths.patch
Patch82: boost-1.66.0-fedora-no-rpath.patch
Patch84: boost-1.66.0-fedora-spirit-abs-overflow.patch
Patch85: boost-1.67.0-upstream-python.patch
Patch87: boost-1.66.0-fedora-numpy3.patch

# we use %%requires_python_ABI, introduced in rpm-build-python-0.36.6-alt1
BuildRequires(pre): rpm-build-python >= 0.36.6-alt1
BuildRequires: python-devel libnumpy-devel

%if_with python3
# we use %%_python3_abiflags
# we use %%requires_python_ABI, introduced in rpm-build-python3-0.1.9.3-alt1
BuildRequires(pre): rpm-build-python3 >= 0.1.9.3-alt1
BuildRequires: python3-devel libnumpy-py3-devel
%endif

%if_with mpi
BuildRequires: %mpiimpl-devel
%endif

#buildreq doesn't do anything sane on this package
BuildRequires: gcc-c++ libstdc++-devel zlib-devel bzlib-devel libicu-devel
#BuildRequires: libexpat-devel-static libexpat-devel

%if_with devel
%description
The Boost web site provides free peer-reviewed portable C++ source
libraries.  The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been included in the C++ 2011 standard and others have been
proposed to the C++ Standards Committee for inclusion in future
standards.

Although Boost was begun by members of the C++ Standards Committee
Library Working Group, membership has expanded to include nearly two
thousand members of the C++ community at large.
%else
%description
This is legacy package build to ease transition to new version of
Boost.
%endif


%if_with devel

%package devel-headers
Summary: Boost libraries header files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

Requires: %name-devel = %epoch:%version-%release

%description devel-headers
The Boost web site provides free peer-reviewed portable C++ source
libraries.  The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been included in the C++ 2011 standard and others have been
proposed to the C++ Standards Committee for inclusion in future
standards.

This package contains header files only.


%package devel
Summary: Boost libraries
Group: Development/C++

PreReq: %name-devel-headers = %epoch:%version-%release
Requires: libboost_atomic%version = %epoch:%version-%release
Requires: libboost_chrono%version = %epoch:%version-%release
Requires: libboost_container%version = %epoch:%version-%release
Requires: libboost_contract%version = %epoch:%version-%release
Requires: libboost_date_time%version = %epoch:%version-%release
Requires: libboost_graph%version = %epoch:%version-%release
Requires: libboost_iostreams%version = %epoch:%version-%release
Requires: libboost_random%version = %epoch:%version-%release
Requires: libboost_regex%version = %epoch:%version-%release
Requires: libboost_serialization%version = %epoch:%version-%release
Requires: libboost_system%version = %epoch:%version-%release
Requires: libboost_test%version = %epoch:%version-%release
Requires: libboost_timer%version = %epoch:%version-%release
Requires: libboost_thread%version = %epoch:%version-%release

Provides: boost-atomic-devel = %epoch:%version-%release
Obsoletes: boost-atomic-devel < %epoch:%version-%release
Provides: boost-chrono-devel = %epoch:%version-%release
Obsoletes: boost-chrono-devel < %epoch:%version-%release
Provides: boost-datetime-devel = %epoch:%version-%release
Obsoletes: boost-datetime-devel < %epoch:%version-%release
Provides: boost-graph-devel = %epoch:%version-%release
Obsoletes: boost-graph-devel < %epoch:%version-%release
Provides: boost-iostreams-devel = %epoch:%version-%release
Obsoletes: boost-iostreams-devel < %epoch:%version-%release
Provides: boost-regex-common-devel = %epoch:%version-%release
Obsoletes: boost-regex-common-devel < %epoch:%version-%release
Provides: boost-regex-devel = %epoch:%version-%release
Obsoletes: boost-regex-devel < %epoch:%version-%release
Provides: boost-regex-gcc2-devel = %epoch:%version-%release
Provides: boost-regex-gcc3-devel = %epoch:%version-%release
Obsoletes: boost-regex-gcc2-devel, boost-regex-gcc3-devel, boost-regex-common-devel
Provides: boost-serialization-devel = %epoch:%version-%release
Obsoletes: boost-serialization-devel < %epoch:%version-%release
Provides: boost-system-devel = %epoch:%version-%release
Obsoletes: boost-system-devel < %epoch:%version-%release
Provides: boost-test-devel = %epoch:%version-%release
Obsoletes: boost-test-devel < %epoch:%version-%release
Provides: boost-timer-devel = %epoch:%version-%release
Obsoletes: boost-timer-devel < %epoch:%version-%release
Provides: boost-thread-devel = %epoch:%version-%release
Obsoletes: boost-thread-devel < %epoch:%version-%release

Provides: %name-intrusive-devel = %epoch:%version-%release
Obsoletes: %name-intrusive-devel < %epoch:%version-%release
Provides: %name-units-devel = %epoch:%version-%release
Obsoletes: %name-units-devel < %epoch:%version-%release

Provides: %name-process-devel = %epoch:%version-%release
Obsoletes: %name-process-devel < %epoch:%version-%release


%description devel
The Boost web site provides free peer-reviewed portable C++ source
libraries.  The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been included in the C++ 2011 standard and others have been
proposed to the C++ Standards Committee for inclusion in future
standards.


%package complete
Summary: Boost libraries -- complete release
Group: Development/C++
BuildArch: noarch

Requires: %name-devel-headers = %epoch:%version-%release
Requires: %name-devel = %epoch:%version-%release
Requires: %name-asio-devel = %epoch:%version-%release
Requires: %name-chrono-devel = %epoch:%version-%release
%if_with context
Requires: %name-context-devel = %epoch:%version-%release
Requires: %name-coroutine-devel = %epoch:%version-%release
%endif
Requires: %name-filesystem-devel = %epoch:%version-%release
Requires: %name-flyweight-devel = %epoch:%version-%release
Requires: %name-geometry-devel = %epoch:%version-%release
%if_with mpi
Requires: %name-graph-parallel-devel = %epoch:%version-%release
%endif
Requires: %name-interprocess-devel = %epoch:%version-%release
Requires: %name-intrusive-devel = %epoch:%version-%release
Requires: %name-locale-devel = %epoch:%version-%release
Requires: %name-lockfree-devel = %epoch:%version-%release
Requires: %name-log-devel = %epoch:%version-%release
Requires: %name-math-devel = %epoch:%version-%release
%if_with mpi
Requires: %name-mpi-devel = %epoch:%version-%release
%endif
Requires: %name-msm-devel = %epoch:%version-%release
Requires: %name-multiprecision-devel = %epoch:%version-%release
Requires: %name-polygon-devel = %epoch:%version-%release
Requires: %name-program_options-devel = %epoch:%version-%release
Requires: %name-python-devel = %epoch:%version-%release
%if_with python3
Requires: %name-python3-devel = %epoch:%version-%release
%endif
Requires: %name-signals-devel = %epoch:%version-%release
Requires: %name-timer-devel = %epoch:%version-%release
Requires: %name-units-devel = %epoch:%version-%release
Requires: %name-wave-devel = %epoch:%version-%release

%description complete
The Boost web site provides free peer-reviewed portable C++ source
libraries.  The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been included in the C++ 2011 standard and others have been
proposed to the C++ Standards Committee for inclusion in future
standards.

This is a virtual package which depends on all Boost packages except
static libraries. Install it if you need complete Boost distribution in
your system.


%package asio-devel
Summary: The Boost Asio Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release

%description asio-devel
asio is a cross-platform C++ library for network programming that
provides developers with a consistent asynchronous I/O model using a
modern C++ approach.


%package context-devel
Summary: The Boost Context Library development files
Group: Development/C++
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release
Requires: libboost_context%version = %epoch:%version-%release

%description context-devel
Boost.Context is a foundational library that provides a sort of
cooperative multitasking on a single thread. By providing an abstraction
of the current execution state in the current thread, including the
stack (with local variables) and stack pointer, all registers and CPU
flags, and the instruction pointer, a fcontext_t instance represents a
specific point in the application's execution path. This is useful for
building higher-level abstractions, like coroutines, cooperative threads
(userland threads) or an equivalent to C# keyword yield in C++.


%package coroutine-devel
Summary: The Boost Coroutine Library development files
Group: Development/C++
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release
Requires: %name-context-devel = %epoch:%version-%release
Requires: libboost_coroutine%version = %epoch:%version-%release

%description coroutine-devel
Boost.Coroutine provides templates for generalized subroutines which
allow multiple entry points for suspending and resuming execution at
certain locations. It preserves the local state of execution and allows
re-entering subroutines more than once (useful if state must be kept
across function calls).

In contrast to threads, which are pre-emptive, coroutine switches are
cooperative (programmer controls when a switch will happen). The kernel
is not involved in the coroutine switches.

The implementation uses Boost.Context for context switching.


%package filesystem-devel
Summary: The Boost Filesystem Library development files
Group: Development/C++
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release
Requires: libboost_filesystem%version = %epoch:%version-%release

%description filesystem-devel
The Boost Filesystem Library provides portable facilities to query and
manipulate paths, files, and directories.


%package flyweight-devel
Summary: The Boost Flyweight Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release
Requires: %name-interprocess-devel = %epoch:%version-%release

%description flyweight-devel
Flyweights are small-sized handle classes granting constant access to
shared common data, thus allowing for the management of large amounts of
entities within reasonable memory limits. Boost.Flyweight makes it easy
to use this common programming idiom by providing the class template
flyweight<T>, which acts as a drop-in replacement for const T.

It is header-only library. This package contains the headers.


%package geometry-devel
Summary: The Boost Geometry Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release
Requires: %name-polygon-devel = %epoch:%version-%release

%description geometry-devel
Boost.Geometry, defines concepts, primitives and algorithms for solving
geometry problems. It Boost.Geometry contains a dimension-agnostic,
coordinate-system-agnostic and scalable kernel, based on concepts,
meta-functions and tag dispatching. On top of that kernel, algorithms
are built.

Boost.Geometry contains instantiable geometry classes, but library
users can also use their own. Using registration macros or traits
classes their geometries can be adapted to fulfil Boost.Geometry
concepts.

It is header-only library. This package contains the headers.


%if_with mpi
%package graph-parallel-devel
Summary: Development files for Parallel Boost Graph Library
Group: Development/C++
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release
Requires: %name-mpi-devel = %epoch:%version-%release
Requires: libboost_graph%version = %epoch:%version-%release
Requires: libboost_graph_parallel%version = %epoch:%version-%release

%description graph-parallel-devel
The Parallel Boost Graph Library is an extension to the Boost Graph
Library (BGL) for parallel and distributed computing. It offers
distributed graphs and graph algorithms to exploit coarse-grained
parallelism along with parallel algorithms that exploit fine-grained
parallelism, while retaining the same interfaces as the (sequential)
BGL.
%endif


%package locale-devel
Summary: The Boost Locale Library development files
Group: Development/C++
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release
Requires: libboost_locale%version = %epoch:%version-%release

%description locale-devel
Boost.Locale is a library that provides high quality localization
facilities in a C++ way. It gives powerful tools for development
of cross platform localized software - the software that talks
to user in its language.


%package lockfree-devel
Summary: The Boost Lockfree Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release

%description lockfree-devel
Boost.Lockfree library provides lockfree data structures, like
lockfree queue and stack.


%package log-devel
Summary: The Boost Locale Library development files
Group: Development/C++
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release
Requires: libboost_log%version = %epoch:%version-%release

%description log-devel
Boost.Log v2 is a library that aims to make logging significantly easier
for the application developer. It provides a wide range of
out-of-the-box tools along with public interfaces for extending the
library.


%package interprocess-devel
Summary: The Boost Interprocess Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release
Requires: %name-intrusive-devel = %epoch:%version-%release

%description interprocess-devel
Boost.Interprocess provides portable access to shared memory, memory
mapped files, process-shared mutexes, condition variables, containers
and allocators.

It is header-only library. This package contains the headers.


# Now boost-intrusive-devel is part of boost-devel-headers,
# as it is required by boost/thread.hpp
#
# %package intrusive-devel
# Summary: The Boost Intrusive Library development files
# Group: Development/C++
# BuildArch: noarch
# AutoReq: yes, nocpp
#
# PreReq: %name-devel = %epoch:%version-%release
#
# %description intrusive-devel
# Boost.Intrusive library provides intrusive containers and algorithms.
#
# It is header-only library. This package contains the headers.


%package math-devel
Summary: The Boost Math Library development files.
Group: Development/C++

PreReq: %name-devel = %epoch:%version-%release
Requires: libboost_math_c99%version = %epoch:%version-%release
Requires: libboost_math_c99f%version = %epoch:%version-%release
%if_with long_double
Requires: libboost_math_c99l%version = %epoch:%version-%release
%endif
Requires: libboost_math_tr1%version = %epoch:%version-%release
Requires: libboost_math_tr1f%version = %epoch:%version-%release
%if_with long_double
Requires: libboost_math_tr1l%version = %epoch:%version-%release
%endif

%description math-devel
The Boost Math Library development files. You'll need to install this
package if you want to link with Boost.Math shared libraries.


%if_with mpi
%package mpi-devel
Summary: The Boost MPI Library development files
Group: Development/C++
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release
PreReq: %name-python-devel = %epoch:%version-%release
Requires: libboost_mpi%version = %epoch:%version-%release
Requires: libboost_mpi_python%version = %epoch:%version-%release
Requires: %mpiimpl-devel

%description mpi-devel
Boost.MPI is a library for message passing in high-performance parallel
applications.
%endif


%package msm-devel
Summary: The Boost MSM Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release

%description msm-devel
Ths Boost Meta State Machine (MSM) is a library allowing you to easily
and quickly define state machines of very high performance.

It is header-only library. This package contains the headers.


%package multiprecision-devel
Summary: The Boost Multiprecision Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release

%description multiprecision-devel
The Multiprecision Library provides integer, rational and floating-point
types in C++ that have more range and precision than C++'s ordinary
built-in types. It consists of a generic interface to the mathematics of
large numbers as well as a selection of big number back ends provided
off-the-rack in including interfaces to GMP, MPFR, MPIR, TomMath as well
as its own collection of Boost-licensed, header-only back ends for
integers, rationals and floats.


%package polygon-devel
Summary: The Boost Polygon Library development files
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release

%description polygon-devel
The Boost.Polygon library provides algorithms focused on manipulating
planar polygon geometry data.  Specific algorithms provided are the
polygon set operations (intersection, union, difference, disjoint-union)
and related algorithms such as polygon connectivity graph extraction,
offsetting and map-overlay.

It is header-only library. This package contains the headers.


%package program_options-devel
Summary: The Boost Filesystem Library development files
Group: Development/C++
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release
Requires: libboost_program_options%version = %epoch:%version-%release

Obsoletes: program_options-devel
Provides: program_options-devel  =  %epoch:%version-%release
Provides: boost-program-options-devel = %epoch:%version-%release

%description program_options-devel
Boost Program Options library allows program developers to obtain
program options, that is (name, value) pairs from the user, via
conventional methods.

%package python-headers
Summary: Boost.Python header files.
Group: Development/C++
BuildArch: noarch
AutoReq: yes, nocpp

%description python-headers
Header files for Boost.Python libraries. This files are shared between
libraries compiled with Python 2 and Python 3.


%package python-devel
Summary: The Boost Python Library (Boost.Python) development files
Group: Development/C++
AutoReq: yes, nocpp

Requires: python-devel = %_python_version
Requires: %name-python-headers = %epoch:%version-%release
Requires: libboost_python%version = %epoch:%version-%release
Requires: libboost_numpy%version = %EVR
PreReq: %name-devel = %epoch:%version-%release

Obsoletes: boost-python-gcc2-devel, boost-python-gcc3-devel, boost-python-common-devel
Provides: boost-python-gcc2-devel = %epoch:%version-%release
Provides: boost-python-gcc3-devel = %epoch:%version-%release
Provides: boost-python-common-devel = %epoch:%version-%release

%description python-devel
Use the Boost Python Library to quickly and easily export a C++ library
to Python such that the Python interface is very similar to the C++
interface. It is designed to be minimally intrusive on your C++ design.
In most cases, you should not have to alter your C++ classes in any way
in order to use them with Boost.Python. The system should simply
``reflect'' your C++ classes and functions into Python.

This package contains development files for Boost.Python build with
Python 2.

%if_with python3
%package python3-devel
Summary: The Boost Python Library (Boost.Python) development files
Group: Development/C++
AutoReq: yes, nocpp

Requires: python3-devel = %_python3_abi_version
Requires: %name-python-headers = %epoch:%version-%release
Requires: libboost_python3-%version = %epoch:%version-%release
Requires: libboost_numpy3-%version = %EVR
PreReq: %name-devel = %epoch:%version-%release

%description python3-devel
Use the Boost Python Library to quickly and easily export a C++ library
to Python such that the Python interface is very similar to the C++
interface. It is designed to be minimally intrusive on your C++ design.
In most cases, you should not have to alter your C++ classes in any way
in order to use them with Boost.Python. The system should simply
``reflect'' your C++ classes and functions into Python.

This package contains development files for Boost.Python build with
Python 3.
%endif

%package signals-devel
Summary: The Boost Signals Library development files
Group: Development/C++
AutoReq: yes, nocpp

PreReq: %name-devel = %epoch:%version-%release
Requires: libboost_signals%version = %epoch:%version-%release

%description signals-devel
The  Boost.Signals  library  is an implementation of a managed signals
and slots  system. Signals represent callbacks with multiple targets,
and  are also called publishers or events in similar systems. Signals
are connected to some set of slots, which are callback receivers (also
called event targets or subscribers), which are called when the signal
is "emitted."


# Now Boost.Units is part of boost-devel-headers.
# See https://svn.boost.org/trac/boost/ticket/4876
#
# %%package units-devel
# Summary: The Boost Units Library development files
# Group: Development/C++
# BuildArch: noarch
# AutoReq: yes, nocpp
#
# PreReq: %name-devel = %epoch:%version-%release
#
# %%description units-devel
# The Boost.Units library is a C++ implementation of dimensional analysis
# and unit/quantity manipulation and conversion.


%package wave-devel
Summary: Boost.Wave Library development files.
Group: Development/C++
AutoReq: yes, nocpp

Requires: libboost_wave%version = %epoch:%version-%release
PreReq: %name-devel = %epoch:%version-%release
Requires: %name-filesystem-devel = %epoch:%version-%release

%description wave-devel
The Boost Wave Library development files.


%package doc
Summary: Boost libraries documentation
Group: Development/C++
BuildArch: noarch

PreReq: %name-devel

%description doc
The Boost web site provides free peer-reviewed portable C++ source
libraries.  The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been included in the C++ 2011 standard and others have been
proposed to the C++ Standards Committee for inclusion in future
standards.

This package contains Boost libraries documentation.
%endif #with devel

%if_with jam
%package jam
License: GPL
Summary: Boost Jam is a replacement for make
Group: Development/Other

%description jam
Boost Jam is a build tool based on FTJam, which in turn is based on
Perforce Jam. It contains significant improvements made to facilitate
its use in the Boost Build System, but should be backward compatible
with Perforce Jam.
%endif


%if_with devel_static
%package devel-static
Summary: Boost libraries
Group: Development/C++

PreReq: %name-devel = %epoch:%version-%release
Requires: %name-atomic-devel = %epoch:%version-%release
Requires: %name-chrono-devel = %epoch:%version-%release
%if_with context
Requires: %name-context-devel = %epoch:%version-%release
%endif
Requires: %name-filesystem-devel = %epoch:%version-%release
%if_with mpi
Requires: %name-graph-parallel-devel = %epoch:%version-%release
Requires: %name-mpi-devel = %epoch:%version-%release
%endif
Requires: %name-locale-devel = %epoch:%version-%release
Requires: %name-log-devel = %epoch:%version-%release
Requires: %name-program_options-devel = %epoch:%version-%release
Requires: %name-python-devel = %epoch:%version-%release
%if_with python3
Requires: %name-python3-devel = %epoch:%version-%release
%endif
Requires: %name-signals-devel = %epoch:%version-%release
Requires: %name-timer-devel = %epoch:%version-%release
Requires: %name-wave-devel = %epoch:%version-%release

Obsoletes: program_options-devel-static
Provides: boost-datetime-devel-static = %epoch:%version-%release
Provides: boost-filesystem-devel-static = %epoch:%version-%release
Provides: boost-graph-devel-static = %epoch:%version-%release
Provides: boost-iostreams-devel-static = %epoch:%version-%release
Provides: boost-program-options-devel-static = %epoch:%version-%release
Provides: boost-python-common-devel-static = %epoch:%version-%release
Provides: boost-python-devel-static = %epoch:%version-%release
Provides: boost-python-gcc2-devel-static = %epoch:%version-%release
Provides: boost-python-gcc3-devel-static = %epoch:%version-%release
Provides: boost-regex-common-devel-static = %epoch:%version-%release
Provides: boost-regex-devel-static = %epoch:%version-%release
Provides: boost-regex-gcc2-devel-static = %epoch:%version-%release
Provides: boost-regex-gcc3-devel-static = %epoch:%version-%release
Provides: boost-serialization-devel-static = %epoch:%version-%release
Provides: boost-signals-devel-static = %epoch:%version-%release
Provides: boost-system-devel-static = %epoch:%version-%release
Provides: boost-test-devel-static = %epoch:%version-%release
Provides: boost-thread-devel-static = %epoch:%version-%release
Provides: boost-wave-devel-static = %epoch:%version-%release
Provides: program_options-devel-static  =  %epoch:%version-%release

%description devel-static
The Boost web site provides free peer-reviewed portable C++ source
libraries.  The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been included in the C++ 2011 standard and others have been
proposed to the C++ Standards Committee for inclusion in future
standards.

This package contains static libraries.
%endif #with devel-static


%package -n libboost_atomic%version
Summary: Boost.Atomic Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_system%version = %epoch:%version-%release
%endif

%description -n libboost_atomic%version
Boost.Atomic is a library that provides atomic data types and operations
on these data types, as well as memory ordering constraints required for
coordinating multiple threads through atomic variables. It implements
the interface as defined by the C++11 standard, but makes this feature
available for platforms lacking system/compiler support for this
particular C++11 feature.


%package -n libboost_chrono%version
Summary: Boost.Chrono Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_system%version = %epoch:%version-%release
%endif

%description -n libboost_chrono%version
Boost.Chrono aims to implement the new time facilities in C++0x,
as proposed in N2661 document. To make the timing facilities of
Boost.Chrono more generally useful, the library provides a number
of clocks that are thin wrappers around the operating system's process
time API, thereby allowing the extraction of wall clock time,
user CPU time, and system CPU time of the process.


%package -n libboost_container%version
Summary: Boost.Container Library
Group: Development/C++

%description -n libboost_container%version
Boost.Container library implements several well-known containers,
including STL containers. The aim of the library is to offers advanced
features not present in standard containers or to offer the latest
standard draft features for compilers that comply with C++03.

%package -n libboost_contract%version
Summary: Boost.Contract Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_system%version = %epoch:%version-%release
%endif

%description -n libboost_contract%version
Boost.Contract library implements contract programming for C++.
All contract programming features are supported:
Subcontracting, class invariants, postconditions (with old and return values),
preconditions, customizable actions
on assertion failure (e.g., terminate or throw),
optional compilation and checking of assertions, etc, from Lorenzo Caminiti. 


%package -n libboost_context%version
Summary: Boost.Context Library
Group: Development/C++

%description -n libboost_context%version
Boost.Context is a foundational library that provides a sort of
cooperative multitasking on a single thread.


%package -n libboost_coroutine%version
Summary: Boost.Coroutine Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_context%version = %epoch:%version-%release
Requires: libboost_thread%version = %epoch:%version-%release
Requires: libboost_system%version = %epoch:%version-%release
%endif

%description -n libboost_coroutine%version
Boost.Coroutine provides templates for generalized subroutines which
allow suspending and resuming execution at certain locations. It
preserves the local state of execution and allows re-entering
subroutines more than once.

Coroutines can be viewed as a language-level construct providing a
special kind of control flow. In contrast to threads, which are
pre-emptive, coroutine switches are cooperative (programmer controls
when a switch will happen). The kernel is not involved in the coroutine
switches. The implementation uses Boost.Context for context switching.


%package -n libboost_date_time%version
Summary: Boost Date-Time Library.
Group: Development/C++
Provides: boost-datetime = %epoch:%version-%release

%description -n libboost_date_time%version
Programming  with  dates  and  times  should  be  almost as simple and
natural  as  programming  with strings and integers. Applications with
lots  of temporal logic can be radically simplified by having a robust
set  of operators and calculation capabilities. Classes should provide
the ability to compare dates and times, add lengths or time durations,
retrieve dates and times from clocks, and work naturally with date and
time intervals.


%package -n libboost_filesystem%version
Summary: Filesystem Library
Group: Development/C++
Provides: boost-filesystem = %epoch:%version-%release

%if_with strict_deps
Requires: libboost_system%version = %epoch:%version-%release
%endif

%description -n libboost_filesystem%version
The Boost Filesystem Library provides portable facilities to query and
manipulate paths, files, and directories.


%package -n libboost_graph%version
Summary: Graph Library
Group: Development/C++
Provides: boost-graph = %epoch:%version-%release

%if_with strict_deps
Requires: libboost_regex%version = %epoch:%version-%release
%endif

%description -n libboost_graph%version
The Boost Graph Library provides  graph components and algorithms.


%if_with mpi
%package -n libboost_graph_parallel%version
Summary: Parallel Boost Graph Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_serialization%version = %epoch:%version-%release
Requires: libboost_mpi%version = %epoch:%version-%release
%endif

%description -n libboost_graph_parallel%version
The Parallel Boost Graph Library is an extension to the Boost Graph
Library (BGL) for parallel and distributed computing. It offers
distributed graphs and graph algorithms to exploit coarse-grained
parallelism along with parallel algorithms that exploit fine-grained
parallelism, while retaining the same interfaces as the (sequential)
BGL.

This package contains shared libraries.
%endif


%package -n libboost_locale%version
Summary: Boost.Locale Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_thread%version = %epoch:%version-%release
Requires: libboost_system%version = %epoch:%version-%release
%endif

%description -n libboost_locale%version
Boost.Locale is a library that provides high quality localization
facilities in a C++ way. It gives powerful tools for development
of cross platform localized software - the software that talks
to user in its language.


%package -n libboost_log%version
Summary: Boost.Log Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_filesystem%version = %epoch:%version-%release
Requires: libboost_regex%version = %epoch:%version-%release
Requires: libboost_thread%version = %epoch:%version-%release
Requires: libboost_system%version = %epoch:%version-%release
%endif

%description -n libboost_log%version
Boost.Log v2 is a library that aims to make logging significantly easier
for the application developer. It provides a wide range of
out-of-the-box tools along with public interfaces for extending the
library.


%package -n libboost_iostreams%version
Summary: I/O streams Library
Group: Development/C++
Provides: boost-iostreams = %epoch:%version-%release

%description -n libboost_iostreams%version
The Boost Iostreams Library provides various iostreams support.


%package -n libboost_math_c99%version
Summary: Boost.Math shared library.
Group: Development/C++
Provides: boost-math = %epoch:%version-%release

%description -n libboost_math_c99%version
Boost.Math shared library.


%package -n libboost_math_c99f%version
Summary: Boost.Math shared library.
Group: Development/C++
Provides: boost-math = %epoch:%version-%release

%description -n libboost_math_c99f%version
Boost.Math shared library.

%if_with long_double
%package -n libboost_math_c99l%version
Summary: Boost.Math shared library.
Group: Development/C++
Provides: boost-math = %epoch:%version-%release

%description -n libboost_math_c99l%version
Boost.Math shared library.
%endif // with long_double


%package -n libboost_math_tr1%version
Summary: Boost.Math shared library.
Group: Development/C++
Provides: boost-math = %epoch:%version-%release

%description -n libboost_math_tr1%version
Boost.Math shared library.


%package -n libboost_math_tr1f%version
Summary: Boost.Math shared library.
Group: Development/C++
Provides: boost-math = %epoch:%version-%release

%description -n libboost_math_tr1f%version
Boost.Math shared library.


%if_with long_double
%package -n libboost_math_tr1l%version
Summary: Boost.Math shared library.
Group: Development/C++
Provides: boost-math = %epoch:%version-%release

%description -n libboost_math_tr1l%version
Boost.Math shared library.
%endif


%if_with mpi
%package -n libboost_mpi%version
Summary: Boost.MPI shared library
Group: Development/C++
Provides: boost-mpi = %epoch:%version-%release
%if_with strict_deps
Requires: libboost_serialization%version = %epoch:%version-%release
%endif

%description -n libboost_mpi%version
Boost.MPI is a library for message passing in high-performance parallel
applications. This package contains shared library.

%package -n libboost_mpi_python%version
Summary: Boost.MPI python shared library
Group: Development/C++
Provides: boost-mpi-python = %epoch:%version-%release
%if_with strict_deps
Requires: libboost_python%version = %epoch:%version-%release
%endif

%requires_python_ABI_for_files %_libdir/*_mpi_python.so.*

%description -n libboost_mpi_python%version
Boost.MPI is a library for message passing in high-performance parallel
applications. This package contains shared library for python bindings.
%endif

%package -n libboost_program_options%version
Summary: The Boost Program_options Library (Boost.Program_options)
Group: Development/C++

Obsoletes: program_options
Provides: program_options = %epoch:%version-%release
Provides: boost-program-options = %epoch:%version-%release

%description -n libboost_program_options%version
The program_options library allows program developers to obtain program
options, that is (name, value) pairs from the user, via conventional
methods such as command line and config file.


%package -n libboost_python%version
Summary: The Boost Python Library (Boost.Python)
Group: Development/C++

Obsoletes: boost-python-gcc2, boost-python-gcc3
Provides: boost-python-gcc2 = %epoch:%version-%release
Provides: boost-python-gcc3 = %epoch:%version-%release
Provides: boost-python = %epoch:%version-%release

# Boost.Python shared libraries have unresolved symbols from libpythonX.X.so.
# This is done intensionally to make it possible to load Python extensions
# written with Boost.Python into programs that link with Python interpreter
# statically (e.g. /usr/bin/python2.7 since 2.7.2-alt5). So, we have to
# convince verify_elf that it is normal. See also thread starting from
# http://lists.altlinux.org/pipermail/devel/2012-April/193731.html
# and especially message where ldv@ suggested this hack (thanks):
# http://lists.altlinux.org/pipermail/devel/2012-April/193827.html
%requires_python_ABI_for_files %_libdir/*boost_python2*.so.*

%description -n libboost_python%version
Use the Boost Python Library to quickly and easily export a C++ library
to Python such that the Python interface is very similar to the C++
interface. It is designed to be minimally intrusive on your C++ design.
In most cases, you should not have to alter your C++ classes in any way
in order to use them with Boost.Python. The system should simply
``reflect'' your C++ classes and functions into Python.

%package -n libboost_numpy%version
Summary: The Boost NumPy Library (Boost.NumPy)
Group: Development/C++
Requires: libboost_python%version = %EVR
Requires: python-module-numpy

%requires_python_ABI_for_files %_libdir/*boost_numpy2*.so.*

%description -n libboost_numpy%version
The Boost.Numpy library exposes quite a few methods to create ndarrays.
ndarrays can be created in a variety of ways,
include empty arrays and zero filled arrays.
ndarrays can also be created from arbitrary python sequences
as well as from data and dtypes.

%if_with python3
%package -n libboost_python3-%version
Summary: The Boost Python Library (Boost.Python) for Python 3
Group: Development/C++

%requires_python3_ABI_for_files %_libdir/*boost_python3*.so.*

%description -n libboost_python3-%version
Use the Boost Python Library to quickly and easily export a C++ library
to Python such that the Python interface is very similar to the C++
interface. It is designed to be minimally intrusive on your C++ design.
In most cases, you should not have to alter your C++ classes in any way
in order to use them with Boost.Python. The system should simply
``reflect'' your C++ classes and functions into Python.

%package -n libboost_numpy3-%version
Summary: The Boost NumPy Library (Boost.NumPy) for Python 3
Group: Development/C++
Requires: libboost_python3-%version = %EVR
Requires: python3-module-numpy

%requires_python3_ABI_for_files %_libdir/*boost_numpy3*.so.*

%description -n libboost_numpy3-%version
The Boost.Numpy library exposes quite a few methods to create ndarrays.
ndarrays can be created in a variety of ways,
include empty arrays and zero filled arrays.
ndarrays can also be created from arbitrary python sequences
as well as from data and dtypes.
%endif

%package -n libboost_random%version
Summary: The Boost.Random library
Group: Development/C++

%description -n libboost_random%version
The Boost Random Number Library (Boost.Random for short) provides
a variety of generators and distributions to produce random numbers
having useful properties.


%package -n libboost_regex%version
Summary: Regular expressions library for C++
Group: Development/C++
Obsoletes: boost-regex-gcc2, boost-regex-gcc3
Provides: boost-regex-gcc2 = %epoch:%version-%release
Provides: boost-regex-gcc3 = %epoch:%version-%release
Provides: boost-regex = %epoch:%version-%release

%description -n libboost_regex%version
Regular expressions are a form of pattern-matching that are often used
in text processing; many users will be familiar with the Unix utilities
grep, sed and awk, and the programming language perl, each of which make
extensive use of regular expressions. Traditionally C++ users have been
limited to the POSIX C API's for manipulating regular expressions, and
while regex++ does provide these API's, they do not represent the best
way to use the library. For example regex++ can cope with wide character
strings, or search and replace operations (in a manner analogous to
either sed or perl), something that traditional C libraries can not do.


%package -n libboost_serialization%version
Summary: The Boost Serialization Library (Boost.Serialization)
Group: Development/C++
Provides: boost-serialization = %epoch:%version-%release

%description -n libboost_serialization%version
Here, we use the term "serialization" to mean the reversible
deconstruction of an arbitrary set of C++ data structures to a sequence
of bytes. Such a system can be used to reconstitute an equivalent
structure in another program context.  Depending on this context, this
might used implement object persistence, remote parameter passing or
other facility.  In this system we use the term "archive" to refer to a
specific rendering of this stream of bytes. This could be a file of
binary data, text data, XML, or some other created by the user of this
library.


%package -n libboost_signals%version
Summary: The Boost Signals Library (Boost.Signals)
Group: Development/C++
Provides: boost-signals = %epoch:%version-%release

%description -n libboost_signals%version
The  Boost.Signals  library  is an implementation of a managed signals
and slots  system. Signals represent callbacks with multiple targets,
and  are also called publishers or events in similar systems. Signals
are connected to some set of slots, which are callback receivers (also
called event targets or subscribers), which are called when the signal
is "emitted."

%package -n libboost_stacktrace%version
Summary: The Boost Stacktrace Library (Boost.Stacktrace)
Group: Development/C++

%description -n libboost_stacktrace%version
Boost.Stacktrace library is a simple C++03 library that provides
information about call sequence in a human-readable form.

%package -n libboost_system%version
Summary: Boost System Library
Group: Development/C++
Provides: boost-system = %epoch:%version-%release

%description -n libboost_system%version
Boost.System library provides operating system support, including
the diagnostics support that will be part of the C++0x standard library.


%package -n libboost_test%version
Summary: Test Library
Group: Development/C++
Provides: boost-test = %epoch:%version-%release

%description -n libboost_test%version
The Boost Test Library provides a matched set of components for writing
test programs, organizing tests in to simple test cases and test suites,
and controlling their runtime execution. The Program Execution Monitor
is also useful in some production (non-test) environments.


%package -n libboost_thread%version
Group: Development/C++
Summary: The Boost Threads Library (Boost.Threads)

%if_with strict_deps
Requires: libboost_system%version = %epoch:%version-%release
%endif

Obsoletes: boost-thread-gcc2, boost-thread-gcc3
Provides: boost-thread-gcc2 = %epoch:%version-%release
Provides: boost-thread-gcc3 = %epoch:%version-%release
Provides: boost-thread = %epoch:%version-%release

%description -n libboost_thread%version
Boost.Threads allows C++ programs to execute as multiple, asynchronous,
independent, threads-of-execution. Each thread has its own machine state
including program instruction counter and registers. Programs which
execute as multiple threads are called multi-threaded programs to
distinguish them from traditional single-threaded programs. Definitions
gives a more complete description of the multi-threading execution
environment.


%package -n libboost_timer%version
Summary: Boost.Timer Library
Group: Development/C++

%if_with strict_deps
Requires: libboost_chrono%version = %epoch:%version-%release
%endif

%description -n libboost_timer%version
Knowing how long a program takes to execute is useful in both test and
production environments.  Boost.Timer provides classes to measures wall
clock time, user CPU process time, system CPU process time, and more.


%package -n libboost_wave%version
Summary: Boost.Wave Library
Group: Development/C++
Provides: boost-wave = %epoch:%version-%release

%if_with strict_deps
Requires: libboost_system%version = %epoch:%version-%release
Requires: libboost_thread%version = %epoch:%version-%release
%endif

%description -n libboost_wave%version
The Boost Wave Library.

%package -n libboost_fiber%version
Summary: Boost.Fiber Library
Group: Development/C++
Provides: boost-fiber = %epoch:%version-%release

%if_with strict_deps
Requires: libboost_context%version = %epoch:%version-%release
%endif

%description -n libboost_fiber%version
The Boost Fiber Library.

%package -n libboost_type_erasure%version
Summary: Boost.TypeErasure Library
Group: Development/C++
Provides: boost-type_erasure = %epoch:%version-%release

%if_with strict_deps
Requires: libboost_system%version = %epoch:%version-%release
Requires: libboost_thread%version = %epoch:%version-%release
%endif

%description -n libboost_type_erasure%version
The Boost TypeErasure Library.

%if_with mpi
%if_with devel
%package -n python-module-boost-mpi
Summary: Boost.MPI python module
Group: Development/Python
%if_with strict_deps
Requires: libboost_mpi%version = %epoch:%version-%release
Requires: libboost_mpi_python%version = %epoch:%version-%release
Requires: libboost_python%version = %epoch:%version-%release
Requires: libboost_serialization%version = %epoch:%version-%release
%endif

%description -n python-module-boost-mpi
Boost.MPI is a library for message passing in high-performance parallel
applications. This package contains python module.

%endif
%endif


%prep

%setup -q -n boost-%version
%patch4 -p2
%patch5 -p2
%patch15 -p1
%patch23 -p2
%patch28 -p3
%patch29 -p2
%patch30 -p1
%patch82 -p1
%patch84 -p1

pushd libs/mpi
%patch85 -p1
popd

%patch87 -p1

COMPILER_FLAGS="%optflags -fno-strict-aliasing"

%ifarch e2k
COMPILER_FLAGS="$COMPILER_FLAGS -fno-error-always-inline"
%endif

cat >> ./tools/build/src/user-config.jam << EOF
# There are many strict aliasing warnings, and it's not feasible to go
# through them all at this time.
using gcc : : : <compileflags>"$COMPILER_FLAGS" ;
%if_with mpi
using mpi ;
%endif
EOF

%build

LINK_BOOST=shared
%if_with devel_static
LINK_BOOST=$LINK_BOOST,static
%endif

%if_with mpi
mpi-selector --yes --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"
%endif

./bootstrap.sh --with-toolset=gcc --with-icu

# Form Fedora spec:
# N.B. When we build the following with PCH, parts of boost (math
# library in particular) end up being built second time during
# installation.  Unsure why that is, but all sub-builds need to be
# built with pch=off to avoid this.
build_boost() {
	[ -n "$NPROCS" ] || NPROCS=%__nprocs
	./b2 -d+2 -q \
	-j$NPROCS \
	--layout=system \
	--toolset=gcc \
	variant=release \
	threading=multi \
	link=$LINK_BOOST \
	optimization=off \
	debug-symbols=off \
	pch=off \
	-sHAVE_ICU=1 \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	"$@" \
	#
}

build_boost \
	--without-python \
%if_without context
	--without-context \
	--without-coroutine \
	--without-fiber \
%endif
	#

cp ./tools/build/src/user-config.jam user-config-py2.jam
cat >> user-config-py2.jam <<'@@@'
using python : %_python_version ;
@@@
build_boost \
	--build-dir=build-py2 \
	--user-config=$PWD/user-config-py2.jam \
	--with-python \
%if_with mpi
	--with-mpi \
%endif
	python=%_python_version

%if_with python3
cp ./tools/build/src/user-config.jam user-config-py3.jam
cat >> user-config-py3.jam <<'@@@'
using python : %_python3_version ;
@@@
build_boost \
	--build-dir=build-py3 \
	--user-config=$PWD/user-config-py3.jam \
	--with-python \
%if_with mpi
	--with-mpi \
%endif
	python=%_python3_version
%endif

%install

LINK_BOOST=shared
%if_with devel_static
LINK_BOOST=$LINK_BOOST,static
%endif

%if_with mpi
mpi-selector --yes --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"
%endif


#libraries and headers are installed by bjam
install_boost() {
	[ -n "$NPROCS" ] || NPROCS=%__nprocs
	./b2 -d+2 -q \
	-j$NPROCS \
	--layout=system \
	--toolset=gcc \
	variant=release \
	threading=multi \
	link=$LINK_BOOST \
	optimization=off \
	debug-symbols=off \
	pch=off \
	-sHAVE_ICU=1 \
	--prefix=%{buildroot}%{_prefix} \
	--libdir=%{buildroot}%{_libdir} \
	"$@" \
	install \
	#
}

install_boost \
	--without-python \
%if_without context
	--without-context \
	--without-coroutine \
	--without-fiber \
%endif
	#

install_boost \
       --build-dir=build-py2 \
       --user-config=$PWD/user-config-py2.jam \
       --with-python \
%if_with mpi
       --with-mpi \
%endif
       python=%_python_version

%if_with python_compat_symlinks
pushd %buildroot%_libdir
ln -s libboost_python%{python_version_nodots python}.so libboost_python.so
ln -s libboost_numpy%{python_version_nodots python}.so libboost_numpy.so
popd
%endif

%if_with python3
install_boost \
	--build-dir=build-py3 \
	--user-config=$PWD/user-config-py3.jam \
	--with-python \
%if_with mpi
	--with-mpi \
%endif
	python=%_python3_version

%if_with python_compat_symlinks
pushd %buildroot%_libdir
ln -s libboost_python%{python_version_nodots python3}.so libboost_python3.so
ln -s libboost_numpy%{python_version_nodots python3}.so libboost_numpy3.so
popd
%endif

%endif

# install mpi python module
%if_with mpi
%if_with devel
mkdir -p %buildroot/%python_sitelibdir/boost
install -Dm644 libs/mpi/build/__init__.py %buildroot/%python_sitelibdir/boost/
mv %buildroot%_libdir/mpi.so %buildroot/%python_sitelibdir/boost/
%else
# The python module won't be created
# if we are a building just library compat pkgs.
# (mpi.so belongs exclusively to the python module.)
rm %buildroot%_libdir/mpi.so
%endif
%endif

%if_with devel

# make symbolic links for compatibility
for i in %buildroot%_libdir/*.so; do
    [ "$i" != "${i%%-st.so}" ] && continue
    ln -s  `basename $i` ${i%%.so}-mt.so
done

%if_without long_double
rm -rf %buildroot%_libdir/*math_c99l*.so*
rm -rf %buildroot%_libdir/*math_tr1l*.so*
%endif

mkdir -p %buildroot%boost_doc

#  install examples
find . -type d -name 'example*' \
    -exec mkdir -p   %buildroot%boost_doc/{} \; \
    -exec sh -c "cp -Rdp {}/* %buildroot%boost_doc/{}" \;

#  install documentation
find . \( -name \*.htm      \
          -or -name \*.html \
          -or -name \*.css  \
          -or -name \*.js   \
          -or -name \*.png  \
          -or -name \*.jpeg \
          -or -name \*.jpg  \
          -or -name \*.svg  \
          -or -name \*.gif  \
          -or -name \*.txt  \
        \) \
        \( -not -name CMakeLists.txt \) \
        -exec install -Dm644 {} %buildroot%boost_doc/{} \;

if [ -d %buildroot%boost_doc/boost ] ; then
    cp -Rdpf %buildroot%boost_doc/boost/* %buildroot%_includedir/%name/
    rm -rf %buildroot%boost_doc/boost
fi

# some documentation have hyperlinks to real headers; this makes them work
ln -s %_includedir/%name %buildroot%boost_doc/boost

# Programs that link with Boost.Thread and Boost.Filesystem need to link
# with Boost.System explicitly. For thread, this is new requirement since
# boost 1.50.0. To avoid breaking build of too many Boost.Thread clients,
# we introduce some linker scripts.

boost_make_linker_script()
{
    local so_path="%buildroot%_libdir/libboost_${1}.so"

    rm -f "${so_path}"
    echo '/* GNU ld script */' > ${so_path}

    echo -n 'GROUP(' >> ${so_path}
    for name in "$@"; do
        echo -n " %_libdir/libboost_${name}.so.%version" >> ${so_path}
    done
    echo ' )' >> ${so_path}
}

boost_make_linker_script thread system
boost_make_linker_script filesystem system
boost_make_linker_script filesystem-st system-st

%endif

%if_with jam
mkdir -p %buildroot%_bindir
install -Dm755 tools/build/src/engine/bjam %buildroot%_bindir
ln -s bjam %buildroot%_bindir/boost-jam
%endif

%if_without devel_static
rm -f %buildroot%_libdir/*.a || :
%endif

#files

%if_with devel
%files devel-headers
%_includedir/%name
%exclude %_includedir/%name/asio*
%if_with context
%exclude %_includedir/%name/context
%exclude %_includedir/%name/coroutine
%endif
%exclude %_includedir/%name/filesystem*
%exclude %_includedir/%name/flyweight*
%exclude %_includedir/%name/geometry*
%exclude %_includedir/%name/interprocess*
# %%exclude %_includedir/%name/intrusive
%exclude %_includedir/%name/locale*
%exclude %_includedir/%name/log/
%exclude %_includedir/%name/lockfree
%if_with mpi
%exclude %_includedir/%name/mpi
%exclude %_includedir/%name/graph/parallel/
%exclude %_includedir/%name/graph/distributed/
%endif
%exclude %_includedir/%name/msm
%exclude %_includedir/%name/multiprecision
%exclude %_includedir/%name/polygon
%exclude %_includedir/%name/program_options*
%exclude %_includedir/%name/python*
%exclude %_includedir/%name/signal*
# %%exclude %_includedir/%name/units*
%exclude %_includedir/%name/wave*

%files devel
%_libdir/*.so
%if_with context
%exclude %_libdir/*_context*.so
%exclude %_libdir/*_coroutine*.so
%endif
%exclude %_libdir/*_filesystem*.so
%exclude %_libdir/*_locale*.so
%exclude %_libdir/*_log*.so
%exclude %_libdir/*_math*.so
%if_with mpi
%exclude %_libdir/*_mpi*.so
%exclude %_libdir/*_graph_parallel*.so
%endif
%exclude %_libdir/*_program_options*.so
%exclude %_libdir/*_python*.so
%exclude %_libdir/*_signals*.so
%exclude %_libdir/*_wave*.so

%dir %boost_doc/
%doc %boost_doc/LICENSE_1_0.txt

%files complete

%files asio-devel
%_includedir/%name/asio*

%if_with context
%files context-devel
%_includedir/%name/context
%_libdir/*_context*.so

%files coroutine-devel
%_includedir/%name/coroutine
%_libdir/*_coroutine*.so
%endif

%files filesystem-devel
%_includedir/%name/filesystem*
%_libdir/*_filesystem*.so

%files flyweight-devel
%_includedir/%name/flyweight*

%files geometry-devel
%_includedir/%name/geometry*

%if_with mpi
%files graph-parallel-devel
%_includedir/%name/graph/parallel/
%_includedir/%name/graph/distributed/
%_libdir/*_graph_parallel*.so
%endif

%files interprocess-devel
%_includedir/%name/interprocess*

# goes to boost-devel-headers
# %%files intrusive-devel
# %_includedir/%name/intrusive

%files locale-devel
%_includedir/%name/locale*
%_libdir/*_locale*.so

%files lockfree-devel
%_includedir/%name/lockfree

%files log-devel
%_includedir/%name/log/
%_libdir/*_log*.so

%files math-devel
#includes go to boost-devel package
#%_includedir/%name/math*
%_libdir/*_math*.so

%if_with mpi
%files mpi-devel
%_includedir/%name/mpi
%_libdir/*_mpi*.so
%endif

%files msm-devel
%_includedir/%name/msm

%files multiprecision-devel
%_includedir/%name/multiprecision

%files polygon-devel
%_includedir/%name/polygon

%files program_options-devel
%_includedir/%name/program_options*
%_libdir/*_program_options*.so

%files python-headers
%_includedir/%name/python*

%files python-devel
%_libdir/*boost_python2*.so
%_libdir/*boost_numpy2*.so
%if_with python_compat_symlinks
%_libdir/libboost_python.so
%_libdir/libboost_python-mt.so
%_libdir/libboost_numpy.so
%_libdir/libboost_numpy-mt.so
%endif

%if_with python3
%files python3-devel
%_libdir/*boost_python3*.so
%_libdir/*boost_numpy3*.so
%endif

%files signals-devel
%_includedir/%name/signal*
%_libdir/*_signals*.so

# %%files units-devel
# %%_includedir/%name/units*

%files wave-devel
%_includedir/%name/wave*
%_libdir/*_wave*.so


%files doc
#everything but license
%doc %boost_doc/[^L]*

%endif #with devel

%if_with jam
%files jam
%_bindir/*
%endif

%if_with devel_static
%files devel-static
%_libdir/*.a
%endif

%files -n libboost_atomic%version
%_libdir/*_atomic*.so.*

%files -n libboost_chrono%version
%_libdir/*_chrono*.so.*

%files -n libboost_container%version
%_libdir/*_container*.so.*

%files -n libboost_contract%version
%_libdir/*_contract*.so.*

%if_with context
%files -n libboost_context%version
%_libdir/*_context*.so.*

%files -n libboost_coroutine%version
%_libdir/*_coroutine*.so.*
%endif

%files -n libboost_date_time%version
%_libdir/*_date_time*.so.*

%files -n libboost_filesystem%version
%_libdir/*_filesystem*.so.*

%files -n libboost_graph%version
%_libdir/*_graph[^_]*so.*

%if_with mpi
%files -n libboost_graph_parallel%version
%_libdir/*_graph_parallel*.so.*
%endif

%files -n libboost_iostreams%version
%_libdir/*_iostreams*.so.*

%files -n libboost_locale%version
%_libdir/*_locale*.so.*

%files -n libboost_log%version
%_libdir/*_log*.so.*

%files -n libboost_math_c99%version
%_libdir/*_math_c99[^lf]*so.*

%files -n libboost_math_c99f%version
%_libdir/*_math_c99f*.so.*

%if_with long_double
%files -n libboost_math_c99l%version
%_libdir/*_math_c99l*.so.*
%endif


%files -n libboost_math_tr1%version
%_libdir/*_math_tr1[^lf]*so.*

%files -n libboost_math_tr1f%version
%_libdir/*_math_tr1f*.so.*

%if_with long_double
%files -n libboost_math_tr1l%version
%_libdir/*_math_tr1l*.so.*
%endif

%if_with mpi
%files -n libboost_mpi%version
%_libdir/*_mpi.so.*

%files -n libboost_mpi_python%version
%_libdir/*_mpi_python.so.*
%endif

%files -n libboost_program_options%version
%_libdir/*_program_options*.so.*

%files -n libboost_python%version
%_libdir/*boost_python2*.so.*

%files -n libboost_numpy%version
%_libdir/*boost_numpy2*.so.*

%if_with python3
%files -n libboost_python3-%version
%_libdir/*boost_python3*.so.*

%files -n libboost_numpy3-%version
%_libdir/*boost_numpy3*.so.*
%endif

%files -n libboost_random%version
%_libdir/*_random*.so.*

%files -n libboost_regex%version
%_libdir/*_regex*.so.*

%files -n libboost_serialization%version
%_libdir/*_serialization*.so.*
%_libdir/*_wserialization*.so.*

%files -n libboost_signals%version
%_libdir/*_signals*.so.*

%files -n libboost_stacktrace%version
%_libdir/*_stacktrace*.so.*

%files -n libboost_system%version
%_libdir/*_system*.so.*

%files -n libboost_test%version
%_libdir/*_test*.so.*
%_libdir/*_prg_exec_monitor*.so.*

%files -n libboost_thread%version
%_libdir/*_thread*.so.*

%files -n libboost_timer%version
%_libdir/*_timer*.so.*

%files -n libboost_wave%version
%_libdir/*_wave*.so.*

%if_with context
%files -n libboost_fiber%version
%_libdir/*_fiber*.so.*
%endif

%files -n libboost_type_erasure%version
%_libdir/*_type_erasure*.so.*

%if_with mpi
%if_with devel
%files -n python-module-boost-mpi
%python_sitelibdir/boost
%endif
%endif

%if_with devel
# Since 1.31.0 and until 1.34.1 /usr/include/boost was a symbolic link
# We have to add this triggers to avoid upgrade problems

%pre devel
if [ -L "%_includedir/%name" ]; then
    mv -f "%_includedir/%name" "%_includedir/%name.BOOST_UPGRADE_RPMSAVE"
fi


%triggerpostun devel -p /bin/bash -- boost-devel

link="%_includedir/%name.BOOST_UPGRADE_RPMSAVE"
if [ -L $link ]; then
    dir=`readlink -f $link`
    echo $dir | grep -q '^/usr/include/boost[_-]1[^/]\+/boost/\?$'
    if [ $? -eq 0 ]; then
        # we have something to delete
        rm -rf $dir
    fi
    rm -f $link
fi

# and one more cleanup
for dir in %_includedir/boost[_-]1*/ ; do
    [ -d $dir/boost ] && rmdir $dir/boost || :
    [ -d $dir ] && rmdir $dir || :
done

%endif #with devel


%changelog
* Mon Dec 10 2018 Ivan A. Melnikov <iv@altlinux.org> 1:1.67.0-alt5
- Make boost-devel replace boost-process-devel.

* Mon Jul 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.67.0-alt4
- Rebuilt with numpy support (Closes: #35190).

* Mon Jun 04 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.67.0-alt3
- Provided compatibility symlinks for boost-python-devel and boost-python3-devel.

* Wed May 30 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.67.0-alt2
- built with MPI support on arm

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.67.0-alt1
- Updated to 1.67.0.
- Packaged libboost_contract.
- Removed libboost_mpi_python3.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.66.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Feb 27 2018 Alexey Shabalin <shaba@altlinux.ru> 1:1.66.0-alt1
- Update to 1.66.0.

* Fri Aug 25 2017 Mikhail Efremov <sem@altlinux.org> 1:1.65.0-alt1
- Fix build without context.
- Package libboost_stacktrace*.
- Package libboost_mpi_python3.
- Use _unpackaged_files_terminate_build.
- Support build for e2k.
- Add with/without context switch.
- Fix build without mpi.
- Use Boost build system v2.
- Updated to 1.65.0.

* Mon Jan 23 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.63.0-alt1
- Updated to 1.63.0.

* Thu May 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.58.0-alt4
- NMU: added patch37 (closes: #32001)

* Fri Apr  1 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.58.0-alt3
- rebuild with python3.5 (for ABI changes)
- this will also rename the autoreqs to the new python3(*) form
- (.spec) fix the build of lib compat pkgs (%%if_without devel)

* Thu Mar 31 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.58.0-alt2
- (.spec) ugly LD_PRELOAD replaced with nice new
  %%requires_python{,3}_ABI_for_files.

* Mon Mar 21 2016 Denis Medvedev <nbr@altlinux.org> 1:1.58.0-alt1.1.2
- (NMU) fix typo in patch that makes errors for python 3.5

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.58.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 09 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.58.0-alt1.1
- Rebuilt with libicui18n.so.56 and libicuuc.so.56.

* Wed May 20 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.58.0-alt1
- Updated to 1.58.0.

* Sun Jan 04 2015 Ivan A. Melnikov <iv@altlinux.org> 1:1.57.0-alt4
- improve Qt4 moc workaround

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1:1.57.0-alt3
- move Boost.Intrusive to boost-devel-headers, as it is now
  required by Boost.Thread;
- fix boost/logic/ packaging (it went to boost-log-devel by mistake).

* Mon Dec 29 2014 Ivan A. Melnikov <iv@altlinux.org> 1:1.57.0-alt2
- correctly mark coroutine-devel subpackage as
  architecture-dependant;
- fix few spelling errors in package summaries and descriptions.

* Sun Dec 28 2014 Ivan A. Melnikov <iv@altlinux.org> 1:1.57.0-alt1
- new version;
- subpackages for new libraries:
  - now Boost.Context and Boost.Coroutine have binaries;
  - Boost.Log was put into separate subpackages;
- import bunch of patches for unused typedefs from Fedora;
- add patch 34 to fix unused typedef in boost/python/cast.hpp;
- drop single-threaded (-st) binaries;
- get rid of version suffix in documentation directory.

* Sat Feb 16 2013 Ivan A. Melnikov <iv@altlinux.org> 1:1.53.0-alt3
- build with python3-3.3.0.

* Sat Feb 09 2013 Ivan A. Melnikov <iv@altlinux.org> 1:1.53.0-alt2
- add patch 29 to make qt4 moc work even when some boost headers
  included.

* Wed Feb 06 2013 Ivan A. Melnikov <iv@altlinux.org> 1:1.53.0-alt1
- new version;
- subpackages for Boost.Atomic, Boost.Coroutine, Boost.Lockfree and
  Boost.Multiprecision.

* Mon Feb 04 2013 Ivan A. Melnikov <iv@altlinux.org> 1:1.52.0-alt2
- fix Boost.Locale UTF issue (CVE-2013-0252).

* Sun Nov 18 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.52.0-alt1
- new version;
- removed patch #27, already applied by upstream;
- fixed packaging for builds without long_double and mpi.

* Mon Oct 01 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.51.0-alt4
- support Python 3 in Boost.Python:
  - a separate library, install boost-python3-devel to build with it;
  - no MPI with Python 3 (yet);
- fix Boost.Polygon build with gcc 4.7 (patch from Scott Tsai).

* Tue Sep 04 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.51.0-alt3
- add patch #27 to make BGL use traits to make null_vertex
  (see https://svn.boost.org/trac/boost/ticket/7327).

* Fri Aug 31 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.51.0-alt2
- fixed headers packaging;
- updated %%description to reflect current state of C++
  standardization (wording taken from fedora package by Petr Machata).

* Thu Aug 30 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.51.0-alt1
- new version;
- new library, Boost.Context, put to separate subpackages;
- updated patches, removed obsolete patches;
- introduced linker scripts for Boost.Thread and Boost.Filesystem.

* Wed Aug 29 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.49.0-alt4
- dirty fix to build with new glibc
  (see https://svn.boost.org/trac/boost/ticket/6940).

* Tue Jun 26 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.49.0-alt3
- rebuild with openmpi 1.6.

* Thu Apr 05 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.49.0-alt2
- don't link libboost_python with libpython.

* Sun Mar 18 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.49.0-alt1
- new version.

* Sat Jan 28 2012 Ivan A. Melnikov <iv@altlinux.org> 1:1.48.0-alt2
- fix compilation when foreach #defined as BOOST_FOREACH (upstream
  ticket 6131) (closes: #26840).

* Mon Nov 28 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.48.0-alt1
- new version;
- packaging updated:
  + Boost.Locale and Boost.Geometry put into separate subpackages;
  + Boost.Chrono development files put into boost-devel;
  + packaged Boost.Timer library;
- updated strict dependencies;
- removed obsolete patch.

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.47.0-alt2.1
- Rebuild with Python-2.7

* Wed Oct 19 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.47.0-alt2
- import patch 25 from Fedora to allow some of Boost.NumericConversion
  functions compile with BOOST_NO_EXCEPTIONS (ALTBUG #26426);
- don't pre-require mpi (ALTBUG #26289);
- wrap everything connected with long double Boost.Math variants with
  if_with long_double (ALTBUG #26289).

* Wed Jul 13 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.47.0-alt1
- new version;
- patches updated;
- Boost.Chrono put into separate subpackage.

* Sat Mar 12 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.46.1-alt1
- new version;
- added patch 24 to fix some missed includes (thx to cpp.req for
  revealing this);
- disabled cpp.req;
- minor spec improvements.

* Fri Mar 11 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.46.0-alt2.1
- fixed build requirements for python:
  + do not pre-require python-devel;
  + pre-require right version of rpm-build-python (thx Myke Lykov
    for reporting a problem with this).

* Sat Feb 26 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.46.0-alt2
- fixed documentation and examples installation regressions.

* Tue Feb 22 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.46.0-alt1
- new version (1.46.0);
- added strict dependencies between sub-packages;
- added missed and removed extra dependencies related to mpi;
- added boost-complete subpackage.

* Sun Jan 02 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.45.0-alt6
- fixed a typo in boost-mpi-devel requirements.

* Sun Jan 02 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.45.0-alt5
- put Parallel Boost Graph Library and it's development files into
  separate subpackages;
- updated patch 23 to disable single-threaded graph_parallel library.

* Sat Jan 01 2011 Ivan A. Melnikov <iv@altlinux.org> 1:1.45.0-alt4
- build Boost.MPI;
- minor spec cleanup.

* Thu Dec 16 2010 Ivan A. Melnikov <iv@altlinux.org> 1:1.45.0-alt3
- rebuild with new icu.

* Mon Nov 22 2010 Ivan A. Melnikov <iv@altlinux.org> 1:1.45.0-alt2
- updated patch 22 to fix rpath issue;
- merged Boost.Units to main devel subpackage, since it's internals
  are used by Boost.Exception (see upstream ticket 4876).

* Sun Nov 21 2010 Ivan A. Melnikov <iv@altlinux.org> 1:1.45.0-alt1
- new version (1.45.0);
- updated patches, removed patches already applied by upstream;
- put new libraries, Boost.MSM and Boost.Polygon, into separate
  subpackages;
- split headers from boost-devel and made them noarch;
- link libboost_python with libpython;
- added subpackage for Boost.Random library;
- minor spec improvements.

* Sat Nov 20 2010 Ivan A. Melnikov <iv@altlinux.org> 1:1.42.0-alt3
- added patch 21 to fix Boost.MPL with gcc 4.5 (closes: #25498);
- fixed installing of examples;
- fixed incorrect Provides: tag in libboost_math*;
- minor spec improvements.

* Mon Feb 08 2010 Alexey Voinov <voins@altlinux.org> 1:1.42.0-alt2
- deps from boost.parameter on boost.python removed

* Thu Feb 04 2010 Alexey Voinov <voins@altlinux.org> 1:1.42.0-alt1
- new version (1.42.0)

* Tue Feb 02 2010 Alexey Voinov <voins@altlinux.org> 1:1.41.0-alt1
- new version (1.41.0)
- multipass-warnings patch is obsolete and removed

* Mon Feb 01 2010 Alexey Voinov <voins@altlinux.org> 1:1.40.0-alt1
- new version (1.40.0)
- exlicit-st patch updated
- function_template patch is obsolete and removed

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.39.0-alt3.1
- Rebuilt with python 2.6

* Sat Jun 13 2009 Ivan A. Melnikov <iv@altlinux.org> 1:1.39.0-alt3
- Added patch #16 from shrek@ to make Boost.Function compile under
  BOOST_NO_EXCEPTIONS. 

* Thu Jun 11 2009 Ivan A. Melnikov <iv@altlinux.org> 1:1.39.0-alt2
- Re-enabled static libraries (closes #20407).

* Wed Jun 03 2009 Ivan A. Melnikov <iv@altlinux.org> 1:1.39.0-alt1
- New version:
  + new libraries since 1.36.0: Flyweight, ScopeExit, Signals2,
    Swap, Proto;
  + lots of bugfixes and improvements in most of libraries.
- Put Boost.Flyweight into separate subpackage.
- Adapted building to new features of Boost.Build with layout=system:
  + following Boost.Build defaults, multi-threaded libraries now
    don't have '-mt' suffix (this means that -lboost_regex brings in
    multi-threaded version of Boost.Regex library);
  + single-threaded libraries have '-st' suffix (updated patch #3,
    put patch #4 back);
  + added "*-mt.so" symbolic links for compatibility with build
    systems which expect older boost libraries naming.
- Removed obsolete patches.
- Several minor spec improvements.

* Wed May 27 2009 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt7
- Added patch #16 with several Boost.Datetime fixes (fixes #20186)

* Fri May 08 2009 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt6
- Added patch #15 from shrek@ to fix building with gcc 4.4

* Fri May 08 2009 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt5
- Added patch #14 which fixes MPL for gcc 4.4.
- Removed obsoletes and provides from asio, because in fact
  Boost.Asio does not provide nor obsoletes asio.

* Fri Dec 12 2008 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt4
- Added sophisticated triggers to fix problems with upgrade
  and workaround strange rpm behaviour.
- Removed obsolete ldconfig-related triggers.
- Added patch 13 to remove some gcc4.3 warnings;
- Added *.gif files to documentation.
- Specfile cleanup and requirements improvements:
  - made development subpackages pre-require boost-devel;
  - added more Obsolete: tags;
  - removed %%__* macros usage.

* Thu Oct 16 2008 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt3
- Added patch 11 by Alex Ott, found in boost trac ticket 2304,
  to fix warinigs in Boost.Spirit (closes #15718)
- Added patch 12 to fix more warnings in Boost.Spirit
- Really applied (not just attached) patches #8-#10

* Mon Sep 29 2008 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt2
- Removed experimental patch 4 and modified spec to get back
  traditional library naming, without -st suffix on single-threaded libs.

* Mon Sep 15 2008 Ivan A. Melnikov <iv@altlinux.org> 1:1.36.0-alt1
- New version (fixes #15168)
- Significantly rewrote specfile to simplify it
- Reviewed libraries separation to reflect interdependencies of boost
  libraries better. This also fixes #15421 and #15397
- Changed build architecture of header-only development packages to noarch
- Changed build layout to system and applied patch from Mandriva
  and our own patch to improve ABI versioning in this case
- Added patch #5, to make location of bjam binary platform-independent.
  This should fix #17004, build on ppc and other platforms as well
- Renamed library packages to confirm Shared Libs Policy
- Joined all static libraries into one package
- Switched to use bjam directly instead of calling configure and make,
  which became insufficient
- Applied all hotfixes from
    https://svn.boost.org/trac/boost/wiki/ReleasePractices/HotFixes
- Removed debug versions of libraries
- Removed patch #1, as it is not needed now
- Removed patch #2, as it was applied by upstream

* Sun Mar 23 2008 Damir Shayhutdinov <damir@altlinux.ru> 1:1.34.1-alt1
- New version

* Tue Feb 05 2008 Damir Shayhutdinov <damir@altlinux.ru> 1:1.34.0-alt5.1
- Applied bga@'s patch for building with python2.5

* Sat Feb 02 2008 Grigory Batalov <bga@altlinux.ru> 1:1.34.0-alt5
- Build without exact python version

* Wed Jan 16 2008 Damir Shayhutdinov <damir@altlinux.ru> 1:1.34.0-alt4
- Fixed invalid memory access in boost-regex++ (thanks ldv@ for noticing)
  + CVE-2008-171
  + CVE-2008-172

* Sun Sep 09 2007 Damir Shayhutdinov <damir@altlinux.ru> 1:1.34.0-alt3
- Provide backward-compatibility symlinks for static libraries (libboost_foo.a->libboost_foo-gcc41-mt.a)

* Tue Jul 03 2007 Damir Shayhutdinov <damir@altlinux.ru> 1:1.34.0-alt2
- Use symlinks, not hardlinks for .so files
- Provide backward-compatibility symlinks for libraries (libboost_foo.so->libboost_foo-gcc41-mt.so)

* Mon May 14 2007 Damir Shayhutdinov <damir@altlinux.ru> 1:1.34.0-alt1
- New version
- New subpackage (graph)

* Sat Apr 07 2007 Damir Shayhutdinov <damir@altlinux.ru> 1:1.33.1-alt4
- boost-devel now requires boost-serialization-devel (#11298)

* Mon Jan 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 1:1.33.1-alt3
- Added missing dependancy for boost-program-options-devel (#10578) 

* Fri Dec 22 2006 Damir Shayhutdinov <damir@altlinux.ru> 1:1.33.1-alt2
- Added missing dependancy for boost-serialization-devel (#10485)

* Thu Sep 14 2006 Damir Shayhutdinov <damir@altlinux.ru> 1:1.33.1-alt1
- New version
- New subpackage (iostreams)

* Mon Apr 25 2005 Anton D. Kachalov <mouse@altlinux.org> 1:1.32.0-alt2
- rebuild with python 2.4
- x86_64 support

* Mon Jan 17 2005 Alexey Voinov <voins@altlinux.ru> 1:1.32.0-alt1
- new version (1.32.0)
- program-options* subpackages added
- serialization subpackage added

* Mon May 24 2004 Alexey Voinov <voins@altlinux.ru> 1:1.31.0-alt2
- builddep on python-devel is now versioned

* Thu Apr 22 2004 Alexey Voinov <voins@altlinux.ru> 1:1.31.0-alt1
- new version (1.31.0)
- license changed to Boost Software License
- Reqs on boost-devel changed to PreReqs to enforce order of installation
- lots of triggers added to provide smooth upgrade

* Mon Aug 25 2003 Alexey Voinov <voins@altlinux.ru> 1:1.30.2-alt1
- new version (1.30.2)

* Wed Aug 13 2003 Alexey Voinov <voins@altlinux.ru> 1:1.30.0-alt1
- new version (1.30.0)
- build system changed, so %%build section does
- added subpackages for datetime, filesystem and test libraries
- description for signals library added
- epoch added (all .so's uses %version as so-version, regex library
  should be updated)
- removed all subpackage specific versions

* Tue Jan 21 2003 Alexey Voinov <voins@voins.program.ru> 1.29.0-alt1
- new version (1.29.0) now we know about g++-3.2
- fixes bug #0001863
- docs added
- new subpackage -signals- added
- boost-threads-devel-static temporarily removed, because static
  libraries for it is not built with boost build system.

* Tue Sep 10 2002 Alexey Voinov <voins@voins.program.ru> 1.28.0-alt0.4
- fixed version numbere for gcc-3.2. 
(this is temporary release)

* Mon Aug 19 2002 Alexey Voinov <voins@voins.program.ru> 1.28.0-alt0.3
- ...-config scripts renamed (s/_/-/g)
- added macros to control compilers version for which to build library

* Sun Aug 18 2002 Alexey Voinov <voins@voins.program.ru> 1.28.0-alt0.2
- spec rewrite: subpackages rearranged, files rearranged
- use gcc-version specific directories instead of update-alternatives
- remake patch updated (soname added)
- pytmake patch updated (soname fixed)
- buildreqs fixed

* Mon Jun 10 2002 Alexey Voinov <voins@voins.program.ru> 1.28.0-alt0.1
- new version (1.28.0)
- .makefile patch split into .remake and .pytmake patches
- buildreqs fixed

* Thu Jun 06 2002 Alexey Voinov <voins@voins.program.ru> 1.27.0-alt0.2
- gcc2/gcc3 variants added for regex subpackages
- /usr/bin/*_config files added
- python subpackages added
- buildreqs fixed


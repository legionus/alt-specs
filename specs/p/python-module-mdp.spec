%define oname mdp

%def_without python3

Name: python-module-%oname
Version: 3.4
Release: alt2.git20140427
Summary: Modular toolkit for Data Processing

Group: Development/Python
License: LGPL-2.0-only
URL: http://mdp-toolkit.sourceforge.net/
# git://github.com/mdp-toolkit/mdp-toolkit
Source: %oname-%version.tar.gz
Source1: MDP-tutorial.pdf
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
%add_python_req_skip test shogun

BuildPreReq: python-devel
BuildPreReq: python-module-scipy
BuildPreReq: libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-scipy libnumpy-py3-devel
BuildPreReq: python-tools-2to3
%endif

Requires: %name-tests = %version-%release

%description
Modular toolkit for Data Processing (MDP) is a Python data processing
framework.

From the user's perspective, MDP is a collection of supervised and
unsupervised learning algorithms and other data processing units that
can be combined into data processing sequences and more complex
feed-forward network architectures.

From the scientific developer's perspective, MDP is a modular framework,
which can easily be expanded. The implementation of new algorithms is
easy and intuitive. The new implemented units are then automatically
integrated with the rest of the library.

The base of available algorithms is steadily increasing and includes, to
name but the most common, Principal Component Analysis (PCA and NIPALS),
several Independent Component Analysis algorithms (CuBICA, FastICA,
TDSEP, JADE, and XSFA), Slow Feature Analysis, Gaussian Classifiers,
Restricted Boltzmann Machine, and Locally Linear Embedding.

%if_with python3
%package -n python3-module-%oname
Summary: Modular toolkit for Data Processing
Group: Development/Python3
%add_python3_req_skip test shogun UserDict
Requires: python3-module-%oname-tests = %version-%release

%description -n python3-module-%oname
Modular toolkit for Data Processing (MDP) is a Python data processing
framework.

From the user's perspective, MDP is a collection of supervised and
unsupervised learning algorithms and other data processing units that
can be combined into data processing sequences and more complex
feed-forward network architectures.

From the scientific developer's perspective, MDP is a modular framework,
which can easily be expanded. The implementation of new algorithms is
easy and intuitive. The new implemented units are then automatically
integrated with the rest of the library.

The base of available algorithms is steadily increasing and includes, to
name but the most common, Principal Component Analysis (PCA and NIPALS),
several Independent Component Analysis algorithms (CuBICA, FastICA,
TDSEP, JADE, and XSFA), Slow Feature Analysis, Gaussian Classifiers,
Restricted Boltzmann Machine, and Locally Linear Embedding.

%package -n python3-module-%oname-tests
Summary: Tests for Modular toolkit for Data Processing
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Modular toolkit for Data Processing (MDP) is a Python data processing
framework.

This package contains tests for MDP.
%endif

%package tests
Summary: Tests for Modular toolkit for Data Processing
Group: Development/Python
Requires: %name = %version-%release

%description tests
Modular toolkit for Data Processing (MDP) is a Python data processing
framework.

This package contains tests for MDP.

%package pickles
Summary: Pickles for Modular toolkit for Data Processing
Group: Development/Python

%description pickles
Modular toolkit for Data Processing (MDP) is a Python data processing
framework.

This package contains pickles for MDP.

%package doc
Summary: Documentation for Modular toolkit for Data Processing
Group: Development/Documentation
BuildArch: noarch

%description doc
Modular toolkit for Data Processing (MDP) is a Python data processing
framework.

This package contains documentation for MDP.

%package -n python-module-binet
Summary: Extension of the pure feed-forward flow concept in MDP
Group: Development/Python
BuildArch: noarch
%add_python_req_skip test

%description -n python-module-binet
The BiNet package is an extension of the pure feed-forward flow concept in MDP.

It defines a framework for far more general flow sequences, involving
top-down processes (e.g. for error backpropagation) or even loops.
So the 'bi' in BiNet primarily stands for 'bidirectional'.

BiNet is implemented by extending both the Node and the Flow concept. Both the
new BiNode and BiFlow classes are 'downward' compatible with the classical
Nodes and Flows, so they can be combined with BiNet elements.

The fundamental addition in BiNet is that BiNodes can specify a target node for
their output and that they can send messages to other nodes. A BiFlow is then
needed to interpret these arguments, e.g. to continue the flow execution at the
specified target node.

BiNet is fully integrated with the HiNet and the Parallel packages. This was
actually one main motivation for creating BiNet, to leverage the modular design
of the other MDP packages.

%package -n python-module-binet-tests
Summary: Tests for the pure feed-forward flow concept in MDP
Group: Development/Python
Requires: python-module-binet = %version-%release

%description -n python-module-binet-tests
The BiNet package is an extension of the pure feed-forward flow concept in MDP.

This package contains tests for BitNet.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

install -p -m644 %SOURCE1 .

%build
%python_build

%if_with python3
pushd ../python3
sed -i 's|#! /usr/bin/env python|#! /usr/bin/env python3|' \
	$(find ./ -name '*.py')
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test
%exclude %python_sitelibdir/bimdp/test

#files pickles
#dir %python_sitelibdir/%oname
#python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/%oname/test
%python_sitelibdir/bimdp/test

%files doc
%doc *.pdf CHANGES CHECKLIST COPYRIGHT
%doc README TODO

#files -n python-module-binet
#python_sitelibdir/binet
#exclude %python_sitelibdir/binet/test

#files -n python-module-binet-tests
#python_sitelibdir/binet/test

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test
%exclude %python3_sitelibdir/bimdp/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test
%python3_sitelibdir/bimdp/test
%endif

%changelog
* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt2.git20140427
- Fixed build

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1.git20140427
- New snapshot

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1.git20130903
- Version 3.4

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1.git20111024
- Version 3.3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2-alt1.git20110415.1
- Rebuild with Python-2.7

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.git20110415
- Version 3.2

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.git20101123
- New snapshot

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.git20100725
- Version 2.6

* Thu Mar 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.svn20091007.2
- Extracted tests into separate packages
- Added
  + pickles package
  + examples

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.svn20091007.1
- Rebuilt with python 2.6

* Fri Oct 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.svn20091007
- Initial build for Sisyphus


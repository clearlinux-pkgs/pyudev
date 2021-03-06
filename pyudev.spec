#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyudev
Version  : 0.22
Release  : 31
URL      : https://github.com/pyudev/pyudev/archive/v0.22/pyudev-0.22.tar.gz
Source0  : https://github.com/pyudev/pyudev/archive/v0.22/pyudev-0.22.tar.gz
Summary  : A libudev binding
Group    : Development/Tools
License  : LGPL-2.1
Requires: pyudev-license = %{version}-%{release}
Requires: pyudev-python = %{version}-%{release}
Requires: pyudev-python3 = %{version}-%{release}
Requires: Sphinx
Requires: docutils
Requires: hypothesis
Requires: pylint
Requires: python-mock
Requires: six
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : hypothesis
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pylint
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
######
pyudev
######
.. image:: https://secure.travis-ci.org/pyudev/pyudev.png?branch=develop
:target: http://travis-ci.org/pyudev/pyudev

%package license
Summary: license components for the pyudev package.
Group: Default

%description license
license components for the pyudev package.


%package python
Summary: python components for the pyudev package.
Group: Default
Requires: pyudev-python3 = %{version}-%{release}

%description python
python components for the pyudev package.


%package python3
Summary: python3 components for the pyudev package.
Group: Default
Requires: python3-core
Provides: pypi(pyudev)
Requires: pypi(six)

%description python3
python3 components for the pyudev package.


%prep
%setup -q -n pyudev-0.22
cd %{_builddir}/pyudev-0.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611951275
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyudev
cp %{_builddir}/pyudev-0.22/COPYING %{buildroot}/usr/share/package-licenses/pyudev/545f380fb332eb41236596500913ff8d582e3ead
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyudev/545f380fb332eb41236596500913ff8d582e3ead

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

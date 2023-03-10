# based on https://src.fedoraproject.org/rpms/pixman/blob/rawhide/f/pixman.spec
Name: pixman
Version: 0.42.2
Release: 3%{?dist}

License: MIT
Summary: Pixel manipulation library
Url: https://xcb.freedesktop.org/

# 0a4e327aef89c25f8cb474fbd01de834fd2a1b13fdf7db11ab72072082e45881cd16060673b59d02054b1711ae69c6e2395f6ae9214225ee7153939efcd2fa5d  pixman-0.42.2.tar.gz
# Sources can be obtained by:
#   wget -c https://cairographics.org/releases/pixman-0.42.2.tar.gz

Source0: https://cairographics.org/releases/%{name}-%{version}.tar.gz

Requires: gtk3
Requires: glibc
Requires: libpng
BuildRequires: gcc
Buildrequires: meson

%description
Pixman: The pixel-manipulation library for X and cairo. 

%package devel
Summary: Pixel manipulation library development package
Requires: pkgconfig
Requires: %{name}%{?isa} = %{version}-%{release}

%description devel 
%summary

%prep
%autosetup -n %{name}-%{version}

%build
%meson --auto-features=auto

%meson_build


%install
%meson_install

%check
%meson_test

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING
%{_libdir}/libpixman-1*.so.*

%files devel
%dir %{_includedir}/pixman-1
%{_includedir}/pixman-1/pixman.h
%{_includedir}/pixman-1/pixman-version.h
%{_libdir}/pkgconfig/pixman-1.pc
%{_libdir}/libpixman-1*.so

%changelog
* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech> 0.42.2-3
- Automatic commit of package [pixman] minor release [0.42.2-2].
  (bader@zaidan.tech)

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech>
- Automatic commit of package [pixman] minor release [0.42.2-2].
  (bader@zaidan.tech)

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech>
- Automatic commit of package [pixman] minor release [0.42.2-2].
  (bader@zaidan.tech)

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech> 0.42.2-2
- correct dependency name (bader@zaidan.tech)

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech>
- correct dependency name (bader@zaidan.tech)

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech>
- correct dependency name (bader@zaidan.tech)

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech>
- correct dependency name (bader@zaidan.tech)

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech> 0.42.2-1
- Automatic commit of package [pixman] minor release [0.42.2-0].
  (bader@zaidan.tech)

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech>
- Automatic commit of package [pixman] minor release [0.42.2-0].
  (bader@zaidan.tech)

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech>
- Automatic commit of package [pixman] minor release [0.42.2-0].
  (bader@zaidan.tech)

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech> 0.42.2-0
- new package built with tito

* Wed Jan 18 2023 Bader Zaidan <bader@zaidan.tech> 0.42.3-1
- new package built with tito


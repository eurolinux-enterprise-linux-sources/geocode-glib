%global json_glib_version 0.99.2

Name:           geocode-glib
Version:        3.14.0
Release:        2%{?dist}
Summary:        Geocoding helper library

License:        LGPLv2+
URL:            http://www.gnome.org/
Source0:        http://download.gnome.org/sources/geocode-glib/3.14/geocode-glib-%{version}.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  json-glib-devel >= %{json_glib_version}
BuildRequires:  libsoup-devel

Requires:       json-glib%{?_isa} >= %{json_glib_version}

%description
geocode-glib is a convenience library for the geocoding (finding longitude,
and latitude from an address) and reverse geocoding (finding an address from
coordinates). It uses Nominatim service to achieve that. It also caches
(reverse-)geocoding requests for faster results and to avoid unnecessary server
load.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

# https://bugzilla.gnome.org/show_bug.cgi?id=1233636
# geocode-glib: should use https://nominatim.gnome.org/
Patch0: use-https-and-fix-the-cache.patch

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%patch0 -p1 -b .use-https-and-fix-the-cache

%build
%configure --disable-static
make %{?_smp_mflags} V=1


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING.LIB NEWS README
%{_libdir}/libgeocode-glib.so.*
%{_libdir}/girepository-1.0/GeocodeGlib-1.0.typelib
%{_datadir}/icons/gnome/scalable/places/*.svg

%files devel
%{_includedir}/geocode-glib-1.0/
%{_libdir}/libgeocode-glib.so
%{_libdir}/pkgconfig/geocode-glib-1.0.pc
%{_datadir}/gir-1.0/GeocodeGlib-1.0.gir
%doc %{_datadir}/gtk-doc/


%changelog
* Fri Jul 24 2015 Zeeshan Ali <zeenix@redhat.com> - 3.14.0-2
- Use HTTPS to connect to Nominatim (related: #1233636).

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.3-2
- Rebuilt for gobject-introspection 1.41.4

* Wed Jun 25 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-1
- Update to 3.12.2

* Wed May 07 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-2
- Ship icons in the main package, instead of -devel

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Wed Mar 19 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92.2-1
- Update to 3.11.92.2

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Tue Mar 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Wed Feb 05 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Wed Jan 15 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4.1-1
- Update to 3.11.4.1

* Tue Sep 24 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0
- Specify minimum json-glib version

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 0.99.4-1
- Update to 0.99.4

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 0.99.3-1
- Update to 0.99.3

* Sat Aug 31 2013 Kalev Lember <kalevlember@gmail.com> - 0.99.2-2
- Move the pkgconfig file to -devel

* Fri Aug 23 2013 Kalev Lember <kalevlember@gmail.com> - 0.99.2-1
- Initial Fedora packaging

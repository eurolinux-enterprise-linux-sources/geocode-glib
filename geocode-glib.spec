%global json_glib_version 0.99.2

Name:           geocode-glib
Version:        3.26.0
Release:        2%{?dist}
Summary:        Geocoding helper library

License:        LGPLv2+
URL:            http://www.gnome.org/
Source0:        http://download.gnome.org/sources/%{name}/3.25/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires:  pkgconfig(libsoup-2.4)

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

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
LANG=en_US.utf8 %meson -Denable-installed-tests=false
LANG=en_US.utf8 %meson_build


%install
LANG=en_US.utf8 %meson_install

# multilib work around for https://gitlab.gnome.org/GNOME/gtk-doc/issues/49
find $RPM_BUILD_ROOT -name '*.html' -exec sed -i -e s,G_MAXINT,G_MAXLONG,g \{\} \;

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING.LIB
%doc AUTHORS NEWS README
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
* Fri Sep 21 2018 Bastien Nocera <bnocera@redhat.com> - 3.26.0-2
+ geocode-glib-3.26.0-2
- Work-around multilib gtk-doc bug
- Resolves: #1624451

* Tue Jun 05 2018 Bastien Nocera <bnocera@redhat.com> - 3.26.0-1
+ geocode-glib-3.26.0-1
- Update to 3.26.0
- Resolves: #1567313

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 3.25.4.1-1
- Update to 3.25.4.1
- Switch to the meson build system
- Resolves: #1567313

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1
- Resolves: #1386868

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

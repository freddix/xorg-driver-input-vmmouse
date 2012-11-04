Summary:	VMMouse protocol for VMware virtual machines
Name:		xorg-driver-input-vmmouse
Version:	12.9.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-vmmouse-%{version}.tar.bz2
# Source0-md5:	2b3bfea9ba1f73d9d68bddd0d6b20112
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-xserver-server-devel
Requires:	xorg-xserver-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VMMouse driver enables support for the special VMMouse protocol
that is provided by VMware virtual machines to give absolute pointer
positioning.

%prep
%setup -qn xf86-input-vmmouse-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	UDEV_RULES_DIR=%{_prefix}/lib/udev/rules.d

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/vmmouse_detect
%attr(755,root,root) %{_libdir}/xorg/modules/input/vmmouse_drv.so

%{_datadir}/X11/xorg.conf.d/50-vmmouse.conf
%{_prefix}/lib/udev/rules.d/69-xorg-vmmouse.rules

%{_mandir}/man1/vmmouse_detect.1*
%{_mandir}/man4/vmmouse.4*


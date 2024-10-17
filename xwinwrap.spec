%define cvs 20060209
%define release 0.%{cvs}.6

Name: xwinwrap
Version: 0
Release: %release
Summary: Utility to run applications as your desktop background
Group: System/X11
URL: https://webcvs.freedesktop.org/xapps/xwinwrap/
Source: %{name}-%{cvs}.tar.bz2
Patch0: xwinwrap-20060209-link.patch
License: GPL
BuildRequires: libx11-devel
BuildRequires: libxext-devel
BuildRequires: libxrender-devel

%description
Wrap, for example, Open GL screen savers and put them on your 
desktop background.

Examples:
xwinwrap -ni -argb -fs -s -st -sp -a -nf -- /usr/lib/xscreensaver/glmatrix \
         -window-id WID
xwinwrap -ni -o 0.6 -fs -s -st -sp -b -nf -- mplayer -wid WID -quiet movie.mpg
xwinwrap -ni -argb -fs -s -st -sp -b -nf -- q3demo -window-id WID

%prep
%setup -q -n %{name}-%{cvs}
%patch0 -p0 -b .link

%build
%setup_compile_flags
%make

%install
mkdir -p %{buildroot}%{_bindir}
cp %{name} %{buildroot}%{_bindir}

%clean

%files
%{_bindir}/%{name}




%changelog
* Fri Jan 21 2011 Funda Wang <fwang@mandriva.org> 0-0.20060209.5mdv2011.0
+ Revision: 632007
- fix linkage and BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0-0.20060209.4mdv2010.0
+ Revision: 435327
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0-0.20060209.3mdv2009.0
+ Revision: 136630
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0-0.20060209.3mdv2008.1
+ Revision: 130624
- kill re-definition of %%buildroot on Pixel's request


(none)
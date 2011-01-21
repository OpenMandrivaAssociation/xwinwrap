%define cvs 20060209
%define release %mkrel 0.%{cvs}.5

Name: xwinwrap
Version: 0
Release: %release
Summary: Utility to run applications as your desktop background
Group: System/X11
URL: http://webcvs.freedesktop.org/xapps/xwinwrap/
Source: %{name}-%{cvs}.tar.bz2
Patch0: xwinwrap-20060209-link.patch
License: GPL
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libx11-devel
BuildRequires: libxext-devel
BuildRequires: libxrender-devel

%description
Wrap, for example, Open GL screen savers and put them on your 
desktop background.

Examples:
xwinwrap -ni -argb -fs -s -st -sp -a -nf -- /usr/lib/xscreensaver/glmatrix -window-id WID
xwinwrap -ni -o 0.6 -fs -s -st -sp -b -nf -- mplayer -wid WID -quiet movie.mpg
xwinwrap -ni -argb -fs -s -st -sp -b -nf -- q3demo -window-id WID

%prep
%setup -q -n %{name}-%{cvs}
%patch0 -p0 -b .link

%build
%setup_compile_flags
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp %{name} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}




Summary:	KDE media player based on mplayer
Summary(pl):	Odtwarzacz mediów dla KDE bazuj±cy na mplayerze
Name:		kplayer
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	3fc9bb78b60f9d21e725feb71a9714b0
URL:		http://sourceforge.net/projects/kplayer/
BuildRequires:	kdelibs-devel >= 3.1
Requires:	kdebase-core
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML
%define		_icondir	%{_datadir}/icons

%description
KPlayer is a KDE media player based on mplayer.

%description -l pl
KPlayer to odtwarzacz mediów dla KDE bazuj±cy na mplayerze.

%prep
%setup -q 

%build

%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_htmldir}

install -d $RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/kplayer.desktop \
    $RPM_BUILD_ROOT%{_desktopdir}

echo "Categories=Qt;KDE;AudioVideo" \
    >> $RPM_BUILD_ROOT%{_desktopdir}/kplayer.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kplayer
%{_datadir}/apps/kplayer
%{_desktopdir}/kplayer.desktop
%{_icondir}/[!l]*/*/apps/*.png

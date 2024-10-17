Name:		texlive-cmathbb
Version:	56414
Release:	2
Summary:	Computer modern mathematical blackboard bold font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cmathbb
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmathbb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmathbb.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This font contains all digits and latin letters uppercase and
lowercase for the Computer Modern font family in blackboard
bold.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cmathbb
%{_texmfdistdir}/fonts/vf/public/cmathbb
%{_texmfdistdir}/fonts/type1/public/cmathbb
%{_texmfdistdir}/fonts/tfm/public/cmathbb
%{_texmfdistdir}/fonts/map/dvips/cmathbb
%{_texmfdistdir}/fonts/enc/dvips/cmathbb
%doc %{_texmfdistdir}/doc/fonts/cmathbb

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

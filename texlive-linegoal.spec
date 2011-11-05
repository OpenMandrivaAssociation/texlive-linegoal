# revision 21523
# category Package
# catalog-ctan /macros/latex/contrib/linegoal
# catalog-date 2011-02-25 20:25:45 +0100
# catalog-license lppl1.3
# catalog-version 2.9
Name:		texlive-linegoal
Version:	2.9
Release:	1
Summary:	A "dimen" that returns the space left on the line
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/linegoal
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linegoal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linegoal.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linegoal.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The linegoal package provides a macro \linegoal to be used with
\setlength: \setlength<some dimen>\linegoal will set <some
dimen> to the horizontal length of the remainder of the line.
This is achieved using the \pdfsavepos primitive of pdftex,
through the zref-savepos package. Example: Some text:
\begin{tabularx}\linegoal{|l|X|} \hline one & two \\ three &
four \\\hline \end{tabularx} will position the table after the
initial text, and make the table fill the rest of the line.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/linegoal/linegoal.sty
%doc %{_texmfdistdir}/doc/latex/linegoal/README
%doc %{_texmfdistdir}/doc/latex/linegoal/linegoal.pdf
#- source
%doc %{_texmfdistdir}/source/latex/linegoal/linegoal.drv
%doc %{_texmfdistdir}/source/latex/linegoal/linegoal.dtx
%doc %{_texmfdistdir}/source/latex/linegoal/linegoal.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

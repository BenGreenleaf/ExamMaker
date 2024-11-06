import fitz, time

pdffile = "D:/Greenleaf & Bowker/Options Arbitrage/physics.pdf"
doc = fitz.open(pdffile)

for page_number in range(1,len(doc)):
    page = doc.load_page(page_number)  # Load the page
    print("Processing page", page_number)

    doc.fullcopy_page(pno=page_number)

    new_page = doc.load_page(len(doc)-1)
    new_page.set_cropbox(fitz.Rect(20, 0, 65, new_page.rect.height))

    pix = new_page.get_pixmap(matrix=fitz.Matrix(150/72, 150/72))  # Get pixmap
    output = f"D:/Greenleaf & Bowker/Options Arbitrage/debugging image{page_number}.png"  # Output file
    pix.save(output)  # Save the pixmap as an image

    locations = []
    for i in range(1,100):
        try:
            #print(new_page.get_textpage().search(str(i)))
            location = round(new_page.get_textpage().search(str(i))[0][0][1],0)
            locations.append(location)
                
        except Exception as e:
            pass

    locations.append(new_page.rect.height)
    print(locations)

    for i in range(0,len(locations)-1):
        height = locations[i]
        doc.fullcopy_page(pno=page_number)
        originalpage = doc.load_page(len(doc)-1)
        originalpage.set_cropbox(fitz.Rect(0, height, originalpage.rect.width, locations[i+1]))  # Set crop box

        pix = originalpage.get_pixmap(matrix=fitz.Matrix(150/72, 150/72))  # Get pixmap
        output = f"D:/Greenleaf & Bowker/Options Arbitrage/outfile{page_number}question{i}.png"  # Output file
        pix.save(output)  # Save the pixmap as an image


#doc.close()


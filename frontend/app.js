const API_URL = 'http://127.0.0.1:5000/api';

// Render Stars
function renderStars(rating) {
    let stars = '';
    for (let i = 0; i < 5; i++) {
        if (i < rating) {
            stars += '★';
        } else {
            stars += '☆';
        }
    }
    return stars;
}

// Fetch and display hotels
async function fetchHotels(searchQuery = '') {
    const grid = document.getElementById('hotelsGrid');
    const loader = document.getElementById('loader');
    
    grid.innerHTML = '';
    loader.style.display = 'block';

    try {
        let url = `${API_URL}/hotels?per_page=100`; 

        const response = await fetch(url);
        if (!response.ok) throw new Error('Failed to fetch data');
        
        const data = await response.json();
        const hotels = data.hotels || [];

        loader.style.display = 'none';

        // Filter if search query exists
        const filteredHotels = hotels.filter(hotel => 
            hotel.name.toLowerCase().includes(searchQuery.toLowerCase()) || 
            hotel.address.toLowerCase().includes(searchQuery.toLowerCase())
        );

        if (filteredHotels.length === 0) {
            grid.innerHTML = `<p style="text-align:center; grid-column: 1/-1; color: var(--text-muted);">Không tìm thấy khách sạn nào.</p>`;
            return;
        }

        filteredHotels.forEach(hotel => {
            // Assign different beautiful unsplash images based on ID for variety
            const imgId = (hotel.id % 5) + 1;
            const images = [
                'https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=800&auto=format&fit=crop',
                'https://images.unsplash.com/photo-1551882547-ff40c0d588fa?q=80&w=800&auto=format&fit=crop',
                'https://images.unsplash.com/photo-1582719508461-905c673771fd?q=80&w=800&auto=format&fit=crop',
                'https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?q=80&w=800&auto=format&fit=crop',
                'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?q=80&w=800&auto=format&fit=crop'
            ];
            
            const imageSrc = images[imgId - 1];

            const card = document.createElement('div');
            card.className = 'hotel-card';
            card.innerHTML = `
                <img src="${imageSrc}" alt="${hotel.name}" class="hotel-image">
                <div class="hotel-info">
                    <div class="hotel-header">
                        <h3 class="hotel-name">${hotel.name}</h3>
                        <div class="hotel-rating">${renderStars(hotel.star_rating)}</div>
                    </div>
                    <div class="hotel-address">
                        📍 ${hotel.address}
                    </div>
                    <p class="hotel-desc">${hotel.description || 'Chưa có mô tả'}</p>
                    <div class="hotel-footer">
                        <div class="hotel-price">Từ 500K <span>/ đêm</span></div>
                        <button class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Đặt Ngay</button>
                    </div>
                </div>
            `;
            grid.appendChild(card);
        });

    } catch (error) {
        loader.style.display = 'none';
        console.error('Error:', error);
        grid.innerHTML = `<p style="text-align:center; grid-column: 1/-1; color: #ef4444;">Lỗi kết nối. Hãy chắc chắn rằng bạn đang bật server Backend (python run.py).</p>`;
    }
}

function searchHotels() {
    const query = document.getElementById('searchInput').value;
    fetchHotels(query);
}

// Initial load
document.addEventListener('DOMContentLoaded', () => {
    fetchHotels();
    
    // Add enter key support for search
    document.getElementById('searchInput').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            searchHotels();
        }
    });
});
